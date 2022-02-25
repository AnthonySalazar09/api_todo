from asyncio import tasks
from traceback import print_tb
from django.conf import settings

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from apps.todo_app.repositories.todo_repository import TodoRepository
from apps.todo_app.serializers.todo_serializer import FolderFullSerializer, FolderSerializer, TaskSerializer


class TodoController(viewsets.ViewSet):
    """
    A Controller for Todo Tasks/Folders.
    """

    def list_folders_by_user_id(self, request, user_id):
        folders = TodoRepository().get_folders_by_user_id(user_id)
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_full_folder_data(self, request, folder_id):
        folder = TodoRepository().get_folder_by_id(folder_id=folder_id)
        serializer = FolderFullSerializer(folder, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_folder(self, request, user_id):
        request.data['user'] = user_id
        serializer = FolderSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        folders = TodoRepository().get_folders_by_user_id(user_id)
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_folder(sefl, request, user_id):
        print(request.data)
        folder = TodoRepository().get_folder_by_id(
            folder_id=request.data['folder'])
        if not folder:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        folder.delete()
        folders = TodoRepository().get_folders_by_user_id(user_id)
        serializer = FolderSerializer(folders, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create_task(self, request, folder_id):
        request.data['folder'] = folder_id
        serializer = TaskSerializer(data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        tasks = TodoRepository().get_tasks_by_folder_id(folder_id=folder_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update_task(self, request, folder_id, task_id):
        task = TodoRepository().get_task_by_id(task_id=task_id)
        if not task:
            return Response({'error', 'task does not exist'}, status=status.HTTP_400_BAD_REQUEST)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        tasks = TodoRepository().get_tasks_by_folder_id(folder_id=folder_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete_task(sefl, request, folder_id, task_id):
        task = TodoRepository().get_task_by_id(task_id=task_id)
        if not task:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)
        task.delete()
        tasks = TodoRepository().get_tasks_by_folder_id(folder_id=folder_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
