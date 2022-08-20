from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status

from tasks.models import Task
from tasks.serializers import TaskSerializer


@api_view(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()

    tasks_serializer = TaskSerializer(tasks, many=True)

    return JsonResponse({"tasks": tasks_serializer.data}, status=status.HTTP_200_OK)
