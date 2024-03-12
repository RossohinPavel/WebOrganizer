from django.shortcuts import render, redirect
from django.http import HttpRequest
from .scripts import asc


def index(request: HttpRequest):
    return redirect(order_view)


# Create your views here.
def order_view(request: HttpRequest):
    return render(request, 'info/order.html')


def report_view(request: HttpRequest):
    return render(request, 'info/report.html')


def asc_view(request: HttpRequest):
    context = {'reports': asc.REPORTS.keys()}

    myfile = request.FILES.get('myfile')
    if request.method == 'POST' and myfile:
        context['tables'] = asc.check_overdue(myfile)

    return render(request, f'info/asc.html', context=context)
