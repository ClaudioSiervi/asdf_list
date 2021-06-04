from django.urls import path
from .views import  TaskListView, TaskDetailView, create_user_view


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='home'),
    path("create-user/", create_user_view, name="create_user"),
    path('tasks/<str:pk>/', TaskDetailView.as_view(), name='detail'),

]
