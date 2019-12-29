from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404
from django.template import loader

from .models import Quote
import random


def index(request):
    ids = Quote.objects.values_list('id', flat=True)
    return single_view(request, random.choice(ids))


def list_view(request):
    quotes_list = Quote.objects.all()
    template = loader.get_template('quotes/list.html')
    context = {
        'quotes': quotes_list,
    }
    return HttpResponse(template.render(context, request))


def single_view(request, quote_id):
    from django.conf import settings
    try:
        quote = get_object_or_404(Quote, id=quote_id)
    except Quote.DoesNotExist:
        raise Http404("Question does not exist")

    template = loader.get_template('quotes/quote.html')
    context = {
        'quote': quote,
        'is_debug': settings.DEBUG,
        'debug_type': str(type(settings.DEBUG))
    }
    return HttpResponse(template.render(context, request))
