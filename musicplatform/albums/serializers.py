from rest_framework import serializers
from .tasks import send
from .models import Album
class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields ='__all__'
    def save(self, **kwargs):
        send.delay(self.validated_data['name'], kwargs['email'])
        return super().save(**kwargs)
    def create(self, validated_data):
        return Album.objects.create(name=validated_data['name'],cost=validated_data['cost'])