from django.urls import path
from .views import  (
CreateFamilytView,
ListFamilyView,
UpdateFamilylView
)


urlpatterns = [
    path('create/', CreateFamilytView.as_view(), name='family-create'),
    path('<str:pk>/', UpdateFamilylView.as_view(), name='family-update'),
    path('', ListFamilyView.as_view(), name='family-list'),
]