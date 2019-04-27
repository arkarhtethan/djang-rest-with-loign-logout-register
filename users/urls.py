from django.urls import path, include
from .routers import router

urlpatterns = [
	
	path('api/', include(router.urls)),
	path('api/rest-auth/', include('rest_auth.urls')),

]