from django.urls import path
from main.views import homePage,loggedOut
app_name = "main"

urlpatterns = [
    path("jobs/", homePage, name='homepage'),
    path('loggedOut/',loggedOut)
]
