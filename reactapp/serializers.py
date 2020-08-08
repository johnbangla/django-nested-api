from rest_framework import serializers
from .models import Task, Album, IImage, Location,CategoryModel



class CategoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
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
    images = ImageSerializer(many=True, read_only=True)
    locations = LocationSerializer(many=True, read_only=True)

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
