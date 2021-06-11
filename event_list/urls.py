from django.urls import path
from .views import  (
    CreateEventView,
    RetrieveEventView,
    ListEventView,  
    UpdateEventlView, 
    DeleteEventView,
)


urlpatterns = [
    path('create/', CreateEventView.as_view(), name='event-create'),
    path('<str:pk>/retrieve/', RetrieveEventView.as_view(), name='event-detail'),
    path('<str:pk>/', UpdateEventlView.as_view(), name='event-update'),
    path('<str:pk>/delete/', DeleteEventView.as_view(), name='event-delete'),
    path('', ListEventView.as_view(), name='event-list'),
]
