import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wic.settings')
project_folder = os.path.expanduser('~/wic.flyhomemn.com/wic/.env')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
application = get_wsgi_application()
