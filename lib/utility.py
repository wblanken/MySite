from django.conf import settings

def activatePage(pageName):
	for p, v in settings.GLOBAL_SETTINGS.page_list.items():
		v = True if p == pageName else False

class pageInfo:
	def __init__(self, name, url, active):
		self.name = name
		self.url = url
		self.active = active
		
	def __hash__(self): return hash(id(self))
		
