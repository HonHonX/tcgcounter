import os
import sys

# Add your project directory to the sys.path
project_home = '/home/YugiohCounter/tcgcounter/countdown_project'
if project_home not in sys.path:
    sys.path.append(project_home)

# Add the directory containing your settings.py to the sys.path
settings_dir = '/home/YugiohCounter/tcgcounter/countdown_project/countdown_project'
if settings_dir not in sys.path:
    sys.path.append(settings_dir)

# Set the environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'countdown_project.settings'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
