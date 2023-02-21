"""
WSGI config for swe1app project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os, sys
from django.core.wsgi import get_wsgi_application

# add the project path into the sys.path
project_path = Path(__file__).resolve().parent
sys.path.append(project_path)

# add the virtualenv site-packages path to the sys.path
sys.path.append('/var/app/venv/*/bin/activate/lib/python3.7/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swe1app.settings')

application = get_wsgi_application()

