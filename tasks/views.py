from rest_framework.decorators import api_view
from django.http.response import JsonResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from tasks.models import Task
from tasks.serializers import TaskSerializer


@api_view(['GET', 'POST'])
def handler_tasks(request):
    if request.method == "GET":
        tasks = Task.objects.all()
        tasks_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse({"tasks": tasks_serializer.data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        task_data = JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse({"task": task_serializer.data}, status=status.HTTP_201_CREATED)
        return JsonResponse(tasks_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", "PUT", "DELETE"])
@csrf_exempt
def handler_tasks_with_pk(request, pk):
    task = None

    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return JsonResponse({"message": "Task not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        task_serializer = TaskSerializer(task)
        return JsonResponse({"task": task_serializer.data}, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        task_parser = JSONParser().parse(request)
        task_serializer = TaskSerializer(task, data=task_parser)
        if task_serializer.is_valid():
            task_serializer.save()
            return JsonResponse({"task": task_serializer.data}, status=status.HTTP_200_OK)
        return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        task.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT)
