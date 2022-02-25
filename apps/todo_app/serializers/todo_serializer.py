from rest_framework import serializers

from apps.todo_app.models import Folder, Task
from apps.todo_app.repositories.todo_repository import TodoRepository


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = (
            'id',
            'folder',
            'title',
            'is_completed',
            'created_at',
            'updated_at',
        )


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = (
            'id',
            'user', 
            'title',
            'created_at',
            'updated_at',
        )


class FolderFullSerializer(serializers.ModelSerializer):
    tasks = serializers.SerializerMethodField('get_tasks')

    class Meta:
        model = Folder
        fields = (
            'id',
            'title',
            'tasks',
            'created_at',
            'updated_at',
        )

    def get_tasks(self, instance):
        tasks = TodoRepository().get_tasks_by_folder_id(folder_id=instance.id)
        serializer = TaskSerializer(tasks, many=True)
        return serializer.data
