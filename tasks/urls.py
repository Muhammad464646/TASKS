from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('tasks', TaskViewSet)

urlpatterns = [
    path('', include(router.urls)), 
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', login_api_view, name='login'),
    path('logout/', logout_api_view, name='logout'),
]
