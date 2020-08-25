from django.http import HttpResponse
from django.template.context_processors import request


def hello(request):
    return HttpResponse("Hello World!");
