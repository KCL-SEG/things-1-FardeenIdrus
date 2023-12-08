from django.urls import path
from .views import things_view

urlpatterns = [
    path('', things_view, name='things'),
]