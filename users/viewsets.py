from .models import CustomUser
from .serializers import CustomUserSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class CustomUserViewSet(viewsets.ModelViewSet):

	serializer_class = CustomUserSerializer

	queryset = CustomUser.objects.all()

	permission_classes = (IsAuthenticatedOrReadOnly,)

	authentication_classes = (TokenAuthentication,)	
