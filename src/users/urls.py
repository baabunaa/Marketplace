from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.log_in_view, name='login'),
    path('registration/', views.registration_view, name='registration'),
]
