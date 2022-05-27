from django.urls import path

from . import views

app_name = "anime"

urlpatterns = [path("list/", views.anime_test, name="anime_list")]
