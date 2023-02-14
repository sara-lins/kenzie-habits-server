from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from .models import Task
from .serializers import TaskSerializer, TaskCheckSerializer

class ListCreateTaskView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class RetrieveUpdateDeleteTaskView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class UpdateTaskView(UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCheckSerializer