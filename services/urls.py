from django.urls import path
from . import views

urlpatterns = [
    path('shariah-advisory/', views.shariah,     name='shariah'),
    path('academy/',          views.academy,     name='academy'),
    path('research-house/',   views.research,    name='research'),
    path('publication/',      views.publication, name='publication'),
]
