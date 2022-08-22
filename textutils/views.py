# This file is not created it is not default 
from django.http import HttpResponse

def index(request):
    return HttpResponse("hello_world")