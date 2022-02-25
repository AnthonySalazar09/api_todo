

from apps.todo_app.models import Folder
from apps.todo_app.models import Task


class TodoRepository():

    def get_folders_by_user_id(self, user_id):
        return Folder.objects.filter(user__id=user_id).order_by('updated_at').all()

    def get_tasks_by_folder_id(self, folder_id):
        return Task.objects.filter(folder__id=folder_id).order_by('updated_at').all()

    def get_folder_by_id(self, folder_id):
        try:
            return Folder.objects.get(id=folder_id)
        except Folder.DoesNotExist:
            return None

    def get_task_by_id(self, task_id):
        try:
            return Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return None
