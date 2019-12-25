from django.shortcuts import render
from django.http import HttpResponse

import os


# Create your views here.
def index(request):
    return HttpResponse(f"Hello world. You're at the quiz page (db user: {os.environ.get('DATABASE_USER')})")
