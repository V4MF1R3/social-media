from django.contrib import admin
from django.urls import path
from app.views.user import CreateUser, LoginUserView, RetrieveUser, UpdateUser

urlpatterns = [
    path('user/create/', CreateUser.as_view()),
    path('user/login/', LoginUserView.as_view()),
    path('user/<int:pk>/', RetrieveUser.as_view()),
    path('user/update/', UpdateUser.as_view()),
]
# comment