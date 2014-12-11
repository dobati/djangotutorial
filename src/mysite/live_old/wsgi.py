import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

from django.core.wsgi import get_wsgi_application

# in video tutorial:
#from django.core.handlers.wsgi import WSGIHandler
# application = WSGIHandler()


application = get_wsgi_application()
