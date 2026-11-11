from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), # grancum enq view-in vor ashxati antery
]
