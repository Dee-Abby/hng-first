from django.urls import path
from .views import basic_info_view


urlpatterns = [
  path('hello/', basic_info_view, name='basic-info')
]
