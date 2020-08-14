from rest_framework import serializers
from .models import Task, Album, IImage, Location,CategoryModel,Parent,Children,Msg
from django.contrib.auth.models import User


#test serilizer







class ChildSerializer(serializers.ModelSerializer):
   

    class Meta:
        model = Children
        fields = ['mobile']


class TestSerializer(serializers.ModelSerializer):
    mobiles = ChildSerializer(many=True)

    class Meta:
        model = Parent
        fields = ['name', 'mobiles']
        
        def create(self, validated_data):
            Children.objects.create(mobiles=Children, **track_data)
          
   


#serilizer

class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        
#This is for dynamic messages
class MsgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Msg
        fields = '__all__'        


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = ['latitude', 'longitude']


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = IImage
        fields = ['url', 'thumbnailUrl', 'aimage', 'bimage']


class AlbumSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True)
    locations = LocationSerializer(many=True)

    class Meta:
        model = Album
        fields = ['id', 'title', 'images', 'price',
                  'categoryId', 'userId', 'locations']

    def create(self, validated_data):
        tracks_data = validated_data.pop('images')
        tracks_data2 = validated_data.pop('locations')

        album = Album.objects.create(**validated_data)
        for track_data in tracks_data:
            IImage.objects.create(album=album, **track_data)

        for track_datae in tracks_data2:
            Location.objects.create(album=album, **track_datae)
        return album


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])

        return user