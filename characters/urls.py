from django.urls import path

from . import views

app_name = "characters"
urlpatterns = [
    path("", views.CharIndexView.as_view(), name = "characters"),
    path("<int:character_id>/", views.character_sheet, name = "character_sheet")
]
