"""
WSGI config for testw project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os, sys

sys.path.insert(0, 'app/testwsgi/testw/testw')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testw.settings')

application = get_wsgi_application()
