from rest_framework import serializers
from .models import User

# class UserSerializer(serializers.Serializer):
#     email = serializers.EmailField(max_length=254)
#     name = serializers.CharField(max_length=100)
    
#     def create(self, validated_data):
        
#         return User.objects.create(validated_data)
    
    
#     class Meta:
#         model = User
#         fields = ['email','name', 'password']

class UserSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = User.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user
    class Meta:
        model = User
        fields = ['email', 'name', 'password']