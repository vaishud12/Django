from rest_framework import serializers
from tags.models import Tag 

class CreateTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag 
        fields = ('name',)
       


class ReadTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','name','slug','created_at',)