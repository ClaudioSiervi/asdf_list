from django.urls import path
from .views import  (
CreateFamilytView,
ListFamilyView
)


urlpatterns = [
    path('create/', CreateFamilytView.as_view(), name='family-create'),

    path('', ListFamilyView.as_view(), name='family-list'),
]