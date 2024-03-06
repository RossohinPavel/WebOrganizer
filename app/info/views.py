from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    info_type = request.GET.get('type', None) or 'order'
    return render(request, f'info/{info_type}.html')