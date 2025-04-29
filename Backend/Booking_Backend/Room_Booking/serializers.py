from rest_framework import serializers

from .models import Room, RoomImage , OccupiedDate, User

class RoomImageSerializer(serializers.ModelSerializer):
    room = serializers.HyperlinkedRelatedField(view_name='room-detail', queryset=Room.objects.all()),
    class Meta:
        model = RoomImage
        fields = ['id','caption','room']

class RoomSerializer(serializers.HyperlinkedModelSerializers):
    images = RoomImageSerializer(many=True, read_only =True)
    class Meta:
        model = Room
        field = ['url','id','name','type', 'maxOccupancy','images']


class OccupiedDateSerializer(serializers.HyperlinkedModelSerializer):
    room  = serializers.HyperlinkedRelatedField(
    view_name = 'room-detail',
    queryset =  Room.objects.all()
    )
    class Meta:
        model = OccupiedDate    
        fields = ['url','id','room','date']
        
        
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = User
        fields = ['url','id','username','password','email','full_name','student_id','phone']
        
    def validate_password(self,value):
        return make_password(value)