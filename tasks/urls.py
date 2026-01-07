from django.urls import path
from .views import (
get_create_category_api_view, edit_delete_category_api_view,
get_create_task_api_view, edit_delete_task_api_view)

urlpatterns = [
    path('add/category', get_create_category_api_view),
    path('edit/category/<int:pk>', edit_delete_category_api_view),
    path('add/task', get_create_task_api_view),
    path('edit/task/<int:pk>', edit_delete_task_api_view),
]