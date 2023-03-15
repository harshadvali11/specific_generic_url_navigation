from django.urls import path
from mi.views import *

app_name='mi'

urlpatterns=[
    path('rohit/',rohit,name='rohit'),
]