from django.templatetags.static import static
from django.urls import path

from django.conf import settings
from main.views import homePage, loggedOut, redirecthome, fillupForm

app_name = "main"

urlpatterns = [
                  path("jobs/", homePage, name='homepage'),
                  path('loggedOut/', loggedOut),
                  path('fillup/<str:uniq_id>', fillupForm.as_view(), name='fillupform'),
                  path('', redirecthome)
              ]
