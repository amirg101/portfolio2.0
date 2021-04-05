
from django.urls import path
from . import views
app_name="portfolio"

urlpatterns = [
    path('',views.index,name="index"),
    path('test/',views.test,name="test"),

    path('projects',views.allprojects,name="pro"),

    path('<str:pk>',views.details,name="details"),


]
