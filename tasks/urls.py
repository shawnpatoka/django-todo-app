from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name="list"),
    path('detail-task/', views.detailTask, name="detail_add"),
    path('update-task/<str:pk>/', views.updateTask, name="update"),
    path('delete-task/<str:pk>/', views.taskDelete, name="delete"),
    path('tick-task/<str:pk>/', views.taskTicked, name="tick_task"),
    path('untick-task/<str:pk>/', views.taskUnticked, name="untick_task"),
    path('search/', views.searchView, name="search"),
    path('go-away/', views.goawayView, name="goaway"),
    path('filter/<str:pk>/', views.filterTasks, name="filter") # working on this right now. Need to change to POST i think.



]