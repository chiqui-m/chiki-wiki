from django.shortcuts import render, redirect

from . import util
import markdown
from random import randint
import string

#LIST of available wikis *********************************************
def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "alphabet": string.ascii_uppercase,
    })

#LIST of available wikis *********************************************
def filter(request, letter):
    print("index_filter")    
    entries = util.search_entries(letter, "firstchar_mode")
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "alphabet": string.ascii_uppercase,
    })

#SHOW the particular or random wiki *********************************************
def wiki(request, title):

    if title == "-random-":
        entries = util.list_entries()
        random_no = randint(1,len(entries))
        title = entries[random_no-1] 

    #retrieve & show the wiki 
    res = util.get_entry(title)

    if res is not None:
        md = markdown.Markdown()
        res_md = md.convert(res)

        return render(request, "encyclopedia/wiki.html", {
            "title":title,
            "content": res_md
        })

    return redirect("index") 

#SEARCH *********************************************
def search(request):
    q = request.POST['searchText']
    entries = util.search_entries(q, "search_mode")
    return render(request, "encyclopedia/search.html", {
        "searchText": q,
        "entries": entries
    })

def search_old(request):
    q = request.POST['searchText']
    q_lower = q.lower()
    allEntries = util.list_entries()
    entries = []

    for e in allEntries:        
        if q_lower in e.lower():
            entries.append(e)
        else:
            content = util.get_entry(e) 
            if q_lower in content.lower():
                entries.append(e)


    return render(request, "encyclopedia/search.html", {
        "searchText": q,
        "entries": entries
    })   


#CREATE a new wiki *********************************************
def new_wiki(request):

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        util.save_entry(title, content)
        return redirect("index")


    return render(request, "encyclopedia/new_wiki.html")


#Edit a wiki *********************************************
def edit_wiki(request, title):

    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']

        util.save_entry(title, content)
        #add to delete the old file if title has changed

        return redirect("index")

    #retrieve & show the wiki 
    res = util.get_entry(title)
    if res is not None:
        return render (request, "encyclopedia/edit_wiki.html", {
            "title" : title,
            "content": res,
            "title_orig":title,
        })
        
    return redirect("index") 
