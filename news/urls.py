from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("article/<int:pk>/", views.article_detail, name="article_detail"),
    path("about-jahizia/", views.about_jahizia, name="about_jahizia"),
]