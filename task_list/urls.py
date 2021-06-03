from django.urls import path
from .views import TaskListView, TaskDetailView


urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='home'),
    path('tasks/<str:pk>/', TaskDetailView.as_view(), name='detail'),
]