from django.urls import path

from . import views

app_name = "mythic"
urlpatterns = [
    path('list_of_games/', views.mythic_games_page, name = 'games_page'),
    
    path("list_of_games/<int:game_id>/", views.game_view, name = "game"),
    
   
    path("list_of_games/<int:game_id>/delete_game/", views.delete_game, name = "delete_game"),
    path("list_of_games/<int:game_id>/<int:scene_id>/messages", views.messages, name = "messages"),
    path("list_of_games/<int:game_id>/notes", views.notes, name = "notes"),
    path("list_of_games/<int:game_id>/scenes", views.scenes, name = 'scenes'),
]
