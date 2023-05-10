from django.urls import path

from . import views

app_name = "mythic"
urlpatterns = [
    path("", views.GameListView.as_view(), name = "list_of_games"),
    path("<int:game_id>/", views.game_view, name = "games"),
    path("get_game/", views.get_more_games, name = "next_game")
]
