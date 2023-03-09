from HARI.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('python/',python,name='python'),
]