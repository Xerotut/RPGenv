from django.urls import path

from . import views

app_name = "accounts"
urlpatterns = [
    path('', views.registrationPage, name = 'registration_page'),
]