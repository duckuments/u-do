from django.urls import include, path
from rest_framework import routers

from .views import *

# define the router
router = routers.DefaultRouter()

# define the router path and viewset to be used
router.register(r'contact-messages', ContactViewSet)
router.register(r'friendships', FriendshipViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'tasks', TaskViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]
