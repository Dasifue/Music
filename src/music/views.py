from django.shortcuts import render
from .models import Band, BandMember, Album, Genre, Song
from django.views import generic
from django.http import HttpResponse

# Create your views here.
def hello_world(request):
    return HttpResponse("hello world")

class AllBandsListView(generic.ListView):
    model = Band
    template_name = "all_bands.html"
    context_object_name = "bands_list"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['second_id'] = Band.objects.filter(id = 2)
    #     return context


class BandInfoView(generic.DetailView):
    model = Band
    template_name = "band_info.html"
