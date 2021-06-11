from django.urls import path
from .views import  (
    create_user_view, 
    TaskCreateView,
    RetrieveTasklView,
    ListTaskView,  
    UpdateTaskView, 
    DeleteTaskView
)


urlpatterns = [

    path("users/", create_user_view, name="user-create"),

    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('<str:pk>/detail/', RetrieveTasklView.as_view(), name='task-detail'),
    path('<str:pk>/', UpdateTaskView.as_view(), name='task-update'),
    path('<str:pk>/delete/', DeleteTaskView.as_view(), name='task-delete'),
    path('', ListTaskView.as_view(), name='task-list'),

    
    

]
