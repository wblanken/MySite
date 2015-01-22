from django.conf import settings
from lib.utility import pageInfo

page = pageInfo('Home', '/', False)

settings.GLOBAL_SETTINGS['page_list'].insert(0,page)

page = pageInfo('About', '/about', False)

settings.GLOBAL_SETTINGS['page_list'].append(page)
