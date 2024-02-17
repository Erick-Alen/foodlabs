from django.urls import path
from .views import UserView, UserDetailedView

urlpatterns = [
    path("users/", UserView.as_view()),
    path("users/<int:user_id>/", UserDetailedView.as_view()),
]
