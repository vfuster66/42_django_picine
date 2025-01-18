from django.contrib import admin
from django.urls import path
from ex00 import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("ex00/", views.markdown_cheatsheet, name="markdown_cheatsheet"),
]
