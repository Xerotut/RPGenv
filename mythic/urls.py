from django.urls import path

from . import views

app_name = "mythic"
urlpatterns = [
    path("", views.GameListView.as_view(), name = "list_of_games"),
    path("<int:game_id>/", views.game_view, name = "games"),
    
    path("get_list_of_games/", views.show_games_list, name = "get_list_of_games"),
    path("delete_game/<int:game_id>/", views.delete_game, name = "delete_game"),
    path("get_game/", views.get_more_games, name = "next_game"),
    path("messages/<int:game_id>/<int:scene_id>/", views.messages, name = "messages"),
    path("send_message/", views.send_message, name = "send_message"),
]
