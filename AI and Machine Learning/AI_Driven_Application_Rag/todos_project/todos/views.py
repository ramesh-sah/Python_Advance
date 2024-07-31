# todos/views.py
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from .models import Todo
from .serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']
