from rest_framework.serializers import ModelSerializer
from users.models import User
class RegistrationSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('email','username','password')
    def create(self,validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        
