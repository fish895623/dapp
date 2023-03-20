from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Todo, Works, WorkTitle, WorkStatus
from .serializers import (
    TodoSerializer,
    WorksSerializer,
    WorkTitleSerializer,
    WorkStatusSerializer,
)


class TodoListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        todos = Todo.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorksListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        works = Works.objects.all()
        serializer = WorksSerializer(works, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorkTitleListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        worktitles = WorkTitle.objects.all()
        serializer = WorkTitleSerializer(worktitles, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class WorkStatusListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        workstatuses = WorkStatus.objects.all()
        serializer = WorkStatusSerializer(workstatuses, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
