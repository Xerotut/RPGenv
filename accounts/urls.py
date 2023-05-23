from django.urls import path

from . import views


urlpatterns = [
    path('registration/', views.registration_page, name = 'registration_page'),
    path('', views.login_page, name = 'login_page'),
]