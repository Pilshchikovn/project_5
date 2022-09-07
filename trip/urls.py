from django.urls import path
from . import views

urlpatterns = [
    path('tours/', views.get_tours),
    path('<int:each_place>/', views.get_info_about_place_by_number),  # конвертер с редиректом
    path('<str:each_place>/', views.get_info_about_place, name='favourite_place'),
    # конвертер + reverce чтобы не хардкодить во view path places
    # path('<each_place>', views.get_info_about_place), #динамичесмкий url со словарем
    # path('new_buyan', views.new_buyan),
    # path('russian_settlement', views.russian_settlement),
    # path('yagodnoe', views.yagodnoe),
    path('', views.allplaces),
]
