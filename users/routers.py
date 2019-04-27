from rest_framework.routers import DefaultRouter
from .viewsets import CustomUserViewSet

router = DefaultRouter()

router.register('user-view-set',CustomUserViewSet)