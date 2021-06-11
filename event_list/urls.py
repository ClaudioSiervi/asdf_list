from django.urls import path
from .views import  (
    CreateEventView,
    RetrieveEventView,
    ListEventView,  
    UpdateEventlView, 
    DeleteEventView,
)


urlpatterns = [
    path('events/create/', CreateEventView.as_view(), name='event-create'),
    path('events/<str:pk>/retrieve/', RetrieveEventView.as_view(), name='event-detail'),
    path('events/<str:pk>/', UpdateEventlView.as_view(), name='event-update'),
    path('events/<str:pk>/delete/', DeleteEventView.as_view(), name='event-delete'),
    path('events/', ListEventView.as_view(), name='event-list'),
]
