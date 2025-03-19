from rest_framework import viewsets
from dashbord.models import *
from home.models import ContactModel
from account.models import *
from .serializers import * 

# home view 
class ContactViewSet(viewsets.ModelViewSet):
    queryset = ContactModel.objects.all()
    serializer_class = ContacMessageSerializer 


# account view : 
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelMessageSerializer 

class FriendshipViewSet(viewsets.ModelViewSet):
    queryset = FriendshipModel.objects.all()
    serializer_class = FriendShipModelMessageSerializer 


# dashbord view : 
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = ProjectModel.objects.all()
    serializer_class = ProjectModelMessageSerializer 

class TaskViewSet(viewsets.ModelViewSet):
    queryset = TaskModel.objects.all()
    serializer_class = TaskModelMessageSerializer 

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class =CategoryModelMessageSerializer 

