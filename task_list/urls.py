from django.urls import path
from .views import  TaskListView, TaskDetailView, create_user_view, create_task_view


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='home'),
    path("create-user/", create_user_view, name="create_user"),
    # path('tasks/<str:pk>/', TaskDetailView.as_view(), name='detail'),
    path('tasks/create/', create_task_view, name='create_task'),
    

]
