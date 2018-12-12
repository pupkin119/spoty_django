from django.urls import path
from . import views

app_name = 'spoty_controller'

urlpatterns = [
    path('', views.login, name = 'spoty_login'),
]