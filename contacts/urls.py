from django.urls import path, include
from contacts import views 
urlpatterns = [
    path("main/", views.home, name="home"),
    path("searchResult/", views.Search, name="fetch"),
    path("find/", views.find, name="find"),
    path("insert/", views.insert, name="insert"),
    path("add/", views.add_data, name="add-a-new-entry"),
    path("del/", views.deleteContact, name="del"),
    path("delete/", views.delete_data, name="del-contact"),
    path("modify/", views.modifyContact, name="modify"),
    path("mod/", views.modify_data, name="mod-contact"),
]