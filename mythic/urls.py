from django.urls import path

from . import views

app_name = "mythic"
urlpatterns = [
    path('', views.mythic_games_page, name = 'games_page'),
    path("get_list_of_games/", views.show_games_list, name = "get_list_of_games"),
    path("<int:game_id>/", views.game_view, name = "games"),
    
   
    path("delete_game/<int:game_id>/", views.delete_game, name = "delete_game"),
    path("messages/<int:game_id>/<int:scene_id>/", views.messages, name = "messages"),
    path("notes/<int:game_id>", views.notes, name = "notes"),
    path("scenes/<int:game_id>/", views.scenes, name = 'scenes'),
]
