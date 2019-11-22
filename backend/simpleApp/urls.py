from django.conf.urls import url, include
from .views import *

app_name = 'simpleApp'

urlpatterns = [
    url(r'^home/', HomePageView.as_view()),
]
