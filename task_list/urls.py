from django.urls import path
from .views import  (
    CreateTaskView,
    RetrieveTasklView,
    ListTaskView,  
    UpdateTaskView, 
    DeleteTaskView,
    update_task_status_view,
)


urlpatterns = [

    path('create/', CreateTaskView.as_view(), name='task-create'),
    path('<str:pk>/retrieve/', RetrieveTasklView.as_view(), name='task-detail'),
    path('<str:pk>/', UpdateTaskView.as_view(), name='task-update'),
    path('<str:pk>/delete/', DeleteTaskView.as_view(), name='task-delete'),
    path('', ListTaskView.as_view(), name='task-list'),
    path('updated_task_status', update_task_status_view, name='task-updade-status'),
    

    
    

]
