from django.urls import path
from .views import  TaskListView, create_user_view, TaskCreateView, TaskUpdatelView, TaskDeleteView


urlpatterns = [
    path('', TaskListView.as_view(), name='task-list'),
    path("users/", create_user_view, name="user-create"),
    # path('tasks/<str:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<str:pk>/', TaskUpdatelView.as_view(), name='task-update'),
    path('tasks/<str:pk>/delete/', TaskDeleteView.as_view(), name='task-delete'),
    path('tasks/', TaskCreateView.as_view(), name='create-task'),
    
    

]
