

from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.ping),
    path('data/<str:code>', views.getData),
    path('delete/<int:id>', views.deleteData),
]