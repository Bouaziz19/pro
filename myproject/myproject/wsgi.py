import os

from django.core.wsgi import get_wsgi_application

import sys
sys.path.append('/var/www/myproject')
sys.path.append('/var/www/myproject/myproject')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")
application = get_wsgi_application()