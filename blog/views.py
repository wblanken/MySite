from django.shortcuts import render
from django.conf import settings

def blog(request):
	return render(request, "blog/base_blog.html", settings.GLOBAL_SETTINGS)
