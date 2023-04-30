from django.urls import path

from . import views

app_name = "characters"
urlpatterns = [
    path("", views.CharIndexView.as_view(), name = "characters"),
    path("<int:pk>/", views.character_sheet, name = "character_sheet"),
    path("save/<int:character_id>/", views.save_character, name = "character_saved")
]
