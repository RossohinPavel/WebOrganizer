from django.urls import path
from . import views


urlpatterns =[
    path('', views.index),
    path('order/', views.order_view),
    path('report/', views.report_view),
    path('asc/', views.asc_view)
]