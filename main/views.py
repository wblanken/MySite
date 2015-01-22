from django.shortcuts import render
from django.conf import settings
from lib.utility import *

def index(request):	
	activatePage("Home")
	return render(request, "main/base_home.html", settings.GLOBAL_SETTINGS)

def about(request):
	activatePage("About")
	return render(request, "main/base_about.html", settings.GLOBAL_SETTINGS)
