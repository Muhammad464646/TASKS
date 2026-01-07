from http.client import responses

from rest_framework import serializers, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Category, Task
from .serialazers import CategorySerializers, TaskSerializers


@api_view(['GET', 'POST'])
def get_create_category_api_view(request):
    if request.method  == 'POST':
        serializer = CategorySerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'errors': "Something was wrong"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'DELETE'])
def edit_delete_category_api_view(request, pk):
    category = Category.objects.filter(id=pk).first()
    if not category:
        return Response('Category does not exists', status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        serializer = CategorySerializers(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = CategorySerializers(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        category.delete()
        return Response({'message': "Category deleted successfully"},status=status.HTTP_204_NO_CONTENT)
    return Response({'errors': "Something was wrong"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET', 'POST'])
def get_create_task_api_view(request):
    if request.method == 'POST':
        serializer = TaskSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        tasks = Task.objects.all()
        serializer = TaskSerializers(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({'errors': "Something was wrong"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH', 'DELETE'])
def edit_delete_task_api_view(request, pk):
    task = Task.objects.filter(id=pk)
    if not task:
        return Response("Task does not exists", status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = TaskSerializers(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        task.delete()
        return Response("Task deleted successfully", status=status.HTTP_204_NO_CONTENT)
    return Response({'errors': "Something was wrong"}, status=status.HTTP_400_BAD_REQUEST)

