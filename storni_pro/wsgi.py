"""
WSGI config for storni_pro project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'storni_pro.settings_dev') # if running in prod, use instead 'storni_pro.settings_prod'

application = get_wsgi_application()
