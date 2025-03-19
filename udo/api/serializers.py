from rest_framework import serializers
from dashbord.models import *
from home.models import ContactModel
from account.models import *

# home
class ContacMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ContactModel 
        fields = "__all__" 


# account 
class UserModelMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User 
        fields = "__all__" 

class FriendShipModelMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FriendshipModel 
        fields = "__all__" 


# dashbord
class ProjectModelMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProjectModel 
        fields = "__all__" 

class TaskModelMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TaskModel 
        fields = "__all__" 

class CategoryModelMessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category 
        fields = "__all__" 
