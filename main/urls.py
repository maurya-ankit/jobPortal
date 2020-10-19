from django.urls import path

from main.views import homePage, loggedOut, redirecthome, fillupForm, detailView

app_name = "main"

urlpatterns = [
    path("jobs/", homePage, name='homepage'),
    path('loggedOut/', loggedOut),
    path("details/<int:id>/", detailView, name='detailed'),
    path('fillup/<str:uniq_id>/', fillupForm.as_view(), name='fillupform'),
    path('', redirecthome)
]
