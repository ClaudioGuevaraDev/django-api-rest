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


@api_view(["GET"])
def get_task(request, pk):
    try:
        task = Task.objects.get(pk=pk)
        task_serializer = TaskSerializer(task)
        return JsonResponse({"task": task_serializer.data}, status=status.HTTP_200_OK)
    except Task.DoesNotExist:
        return JsonResponse({"message": "Task not found."}, status=status.HTTP_404_NOT_FOUND)
