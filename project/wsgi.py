"""
WSGI config for project project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
<<<<<<< HEAD
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
=======
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
>>>>>>> 7d5f087c4e99aa85f4ff913899c3075425769d76
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

application = get_wsgi_application()
