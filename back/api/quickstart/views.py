from rest_framework import status
from rest_framework.response import Response
from api.quickstart.models import Task

from api.quickstart.serializers import TaskSerializer
from rest_framework import viewsets






class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed, created, edited or deleted.
    """
    queryset = Task.objects.all().order_by('name')
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = Task.objects.all()
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)