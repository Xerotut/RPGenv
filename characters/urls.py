from django.urls import path

from . import views

app_name = "characters"
urlpatterns = [
    path("", views.character_list, name = "Characters"),
    path("<int:character_id>/", views.character_sheet, name = "character_sheet")
]
