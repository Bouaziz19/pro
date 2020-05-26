import os
import sys

path='/root/myproject'

if path not in sys.path:
  sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'myproject.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()