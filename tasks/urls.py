from django.urls import path
from .views import ListCreateTaskView, RetrieveUpdateDeleteTaskView, UpdateTaskView

urlpatterns = [
    path('task/', ListCreateTaskView.as_view()),
    path('task/<pk>/', RetrieveUpdateDeleteTaskView.as_view()),
    path('task/check/<pk>/', UpdateTaskView.as_view())
]