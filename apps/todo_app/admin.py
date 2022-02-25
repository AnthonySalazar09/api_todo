from django.contrib import admin

from apps.todo_app.models import Folder
from apps.todo_app.models import Task


admin.site.register(Folder)
admin.site.register(Task)
