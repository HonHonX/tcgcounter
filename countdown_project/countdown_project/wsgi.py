import os
import sys

# Add your project directory to the sys.path
project_home = '/home/YugiohCounter/tcgcounter/countdown_project'
if project_home not in sys.path:
    sys.path.append(project_home)

# Set the environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'countdown_project.settings'

# Activate your virtual environment (if you created one)
activate_env = os.path.expanduser("/home/YugiohCounter/venv/bin/activate_this.py")
exec(open(activate_env).read(), {'__file__': activate_env})

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
