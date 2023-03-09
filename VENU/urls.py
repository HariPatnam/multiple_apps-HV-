from VENU.views import *

from django.urls import path

app_name='nothing'

urlpatterns=[
    path('java/',java,name='java'),
]