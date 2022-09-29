

from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    
    path('', views.ping),
    path('data/<str:code>', views.getData),
    path('delete/<int:id>', views.deleteData),
    path('index/', TemplateView.as_view(template_name='index.html')),

]