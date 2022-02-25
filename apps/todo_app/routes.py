from django.urls import re_path, path

from apps.todo_app.controllers.todo_controller import TodoController


urlpatterns = [
    path('folder/user/<int:user_id>', TodoController.as_view(
        {'get': 'list_folders_by_user_id', 'post': 'create_folder',
         'delete': 'delete_folder'}), name='folder_user'),
    path('folder/user/<int:user_id>/delete/', TodoController.as_view(
        {'post': 'delete_folder'}), name='delete_folder'),
    path('folder/<int:folder_id>',
         TodoController.as_view({'get': 'get_full_folder_data', 'post': 'create_task'}), name='folder_detail'),
    path('folder/<int:folder_id>/task/<int:task_id>',
         TodoController.as_view({'post': 'update_task','get': 'delete_task'}), name='folder'),
]
