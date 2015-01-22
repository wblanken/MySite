from django.shortcuts import render
from django.conf import settings
from lib import utility

def blog(request):
	activatePage('blog')
	pageSettings = settings.GLOBAL_SETTINGS.copy()
	return render(request, "blog/base_blog.html", pageSettings)
