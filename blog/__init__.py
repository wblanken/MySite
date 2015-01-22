from django.conf import settings
from lib.utility import pageInfo

page = pageInfo('Blog', '/blog', False)

settings.GLOBAL_SETTINGS['page_list'].insert(1,page)
