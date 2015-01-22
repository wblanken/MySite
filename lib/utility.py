from django.conf import settings

def activatePage(pageName):
	for p, v in settings.GLOBAL_SETTINGS.page_list.items():
		v = true if p == pagename else false

class pageInfo:
	def __init__(self, name, url, active):
		self.name = name
		self.url = url
		self.active = active
		
	def __hash__(self): return hash(id(self))
		
