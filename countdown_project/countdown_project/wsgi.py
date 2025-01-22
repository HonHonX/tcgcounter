import os
import sys

# Add the path to your project
path = '/home/YugiohCounter/countdown_project'
if path not in sys.path:
    sys.path.append(path)

# Set the Django settings module
os.environ['DJANGO_SETTINGS_MODULE'] = 'countdown_project.settings'

# Import Django and start the application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
