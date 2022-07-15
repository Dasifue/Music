from django.urls import path
from .views import *

app_name = 'authe'


urlpatterns = [
    path('register/', register, name = "register"),
    path('login/', login_view, name='login'),
    path('logout', logout_view, name='logout')
]