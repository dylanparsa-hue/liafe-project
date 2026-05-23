from django.urls import path
from . import views

urlpatterns = [
    path('<slug:slug>/', views.custom_page, name='custom_page'),
]
