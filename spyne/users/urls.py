from django.urls import path
from .views import (
    UserCreateView,
    UserUpdateView,
    UserDeleteView,
    UserListView,
    UserSearchView,
)

urlpatterns = [
    path("", UserListView.as_view(), name="users-list"),
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("<int:id>/update/", UserUpdateView.as_view(), name="user-update"),
    path("<int:id>/delete/", UserDeleteView.as_view(), name="user-delete"),
    path("search/<str:name>/", UserSearchView.as_view(), name="user-search"),
]
