from django.shortcuts import render
from mapbox import Directions
# Create your views here.

def default_maps(request):
	# TODO: move Token to settings.py file
	mapbox_access_token = 'pk.eyJ1IjoidGVjaG1hbmlhY2MiLCJhIjoiY2xjNHNtdm52MGlxajNwbW9mM2ExcGFldSJ9.9T58lzofF1W-FCtKLhAkuA'
	
	return render(request, 'details.html', {'mapbox_access_token':mapbox_access_token})
	