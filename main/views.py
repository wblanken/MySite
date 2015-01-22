from django.shortcuts import render
from django.conf import settings

def index(request):	
	return render(request, "main/base_home.html", settings.GLOBAL_SETTINGS)

def about(request):
	return render(request, "main/base_about.html", settings.GLOBAL_SETTINGS)
