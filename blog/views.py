from django.shortcuts import render
from django.conf import settings
from lib.utility import *

def blog(request):
	activatePage('Blog')
	return render(request, "blog/base_blog.html", settings.GLOBAL_SETTINGS)
