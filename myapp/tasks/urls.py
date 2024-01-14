from django.urls import path
from .views import TaskListView, task_detail, task_create, task_update, task_delete

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:task_id>/', task_detail, name='task_detail'),
    path('tasks/create/', task_create, name='task_create'),
    path('tasks/<int:task_id>/update/', task_update, name='task_update'),
    path('tasks/<int:task_id>/delete/', task_delete, name='task_delete'),
]
