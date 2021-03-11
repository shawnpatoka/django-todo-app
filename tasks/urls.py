from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="list"),
    path('update-task/<str:pk>/', views.updateTask, name="update"),
    path('delete-task/<str:pk>/', views.taskDelete, name="delete"),
    path('tick-task/<str:pk>/', views.taskTicked, name="tick_task"),
    path('untick-task/<str:pk>/', views.taskUnticked, name="untick_task"),

]