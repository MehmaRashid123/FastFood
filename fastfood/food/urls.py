from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),           # Homepage route
    path('menu/', views.menu, name='menu'),
     path('deals/', views.deals_view, name='deals'), 
      path('contact/', views.contact_view, name='contact'),
]
