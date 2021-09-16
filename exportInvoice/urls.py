from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('allBills', views.showBills, name='allBills'),
    path('pdf', views.showPdf, name=''),
    path('changeDescription', views.changeDescription, name=''),
]
