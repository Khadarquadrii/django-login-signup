from django.urls import *
from login.views import *

app_name='login'

urlpatterns=[
    path('login/',login,name='login'),
]