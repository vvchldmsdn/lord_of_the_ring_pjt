from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list),
    path('/race/<str:race_name>', views.get_race_list),
    path('/character/<str:character_name>', views.get_character_detail)
]
