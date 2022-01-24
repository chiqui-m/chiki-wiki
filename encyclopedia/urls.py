from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("filter/<letter>", views.filter, name="filter"),
    path("wiki/<title>", views.wiki, name="wiki"),
    path("edit/<title>/<title_orig>", views.edit_wiki, name="edit_wiki"),
    path("search", views.search, name="search"),
    path("new", views.new_wiki, name="new_wiki")
]
