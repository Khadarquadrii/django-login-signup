from django.urls import *
from signup.views import *

app_name='signup'

urlpatterns=[
    path('signup/',signup,name='signup'),
]