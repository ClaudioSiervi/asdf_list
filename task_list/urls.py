from django.urls import path
from .views import  TaskListView, create_user_view


urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    # path("create-user/", CreateUserListView.as_view(), name="create_user"),
    path("create-user/", create_user_view, name="create_user"),
]