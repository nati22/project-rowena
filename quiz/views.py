from django.http import HttpResponse

import os


# Create your views here.
def index(request):
    return HttpResponse(f"Hello world. You're at the quiz page ({os.environ.get('DEBUG')})")


def config(request):
    return HttpResponse(f"""
    DEBUG = \'{os.environ.get('DEBUG')}\'\n
    DATABASE_NAME = \'{os.environ.get('DATABASE_NAME')}\'\n
    DATABASE_URL = \'{os.environ.get('DATABASE_URL')[:20] if os.environ.get('DATABASE_URL') else None}\'\n
    DATABASE_USER = \'{os.environ.get('DATABASE_USER')}\'\n
    DEBUG_COLLECTSTATIC = \'{os.environ.get('DEBUG_COLLECTSTATIC')}\'\n
    DISABLE_COLLECTSTATIC = \'{os.environ.get('DISABLE_COLLECTSTATIC')}\'\n
    """, content_type="text/plain")
