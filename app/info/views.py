from django.shortcuts import render
from django.http import HttpRequest
from .scripts import asc


# Create your views here.
def index(request: HttpRequest):
    _type = request.GET.get('type', None) or request.POST.get('type', None) or 'order'
    match _type:
        case 'asc':
            return asc_index(request)
        case _:
            return render(request, f'info/{_type}.html')


def asc_index(request: HttpRequest):
    context = {'reports': asc.REPORTS.keys()}
    return render(request, f'info/asc.html', context=context)
