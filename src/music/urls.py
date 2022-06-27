from django.urls import path
from .views import *

app_name = 'music'

urlpatterns = [
    path('', AllBandsListView.as_view(), name = "all_bands"),
    path('band_info/<int:pk>', BandInfoView.as_view(), name = "band_info")
]