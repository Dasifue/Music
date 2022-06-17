from django.urls import path
from .views import *

app_name = 'music'

urlpatterns = [
    path('', hello_world, name = "hello_world")
]