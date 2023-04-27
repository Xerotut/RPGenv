from django.urls import path

from . import views

app_name = "characters"
urlpatterns = [
    path("", views.CharIndexView.as_view(), name = "characters"),
    path("<int:pk>/", views.CharSheetView.as_view(), name = "character_sheet")
]
