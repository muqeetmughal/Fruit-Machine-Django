"""
APP's local routes
"""
from django.urls import path

from . import views

app_name = 'fruit_machine'

urlpatterns = [
    path('', views.index, name='index'),
    path('draw', views.draw_spin, name='draw_spin'),
    path('<int:pk>', views.draw_result, name='draw_result'),
]
