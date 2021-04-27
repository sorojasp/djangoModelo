from rest_framework import serializers

from profiles_app import models

class HelloSerializer(serializers.Serializer):
    """Serializers a name field for testing our APIView"""
    name=serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile project"""
    class Meta:
        model=models.UserProfile
        fields=('email','password',)
        extra_kwargs={
            'password': {
                'write_only':True,
                'style':{
                    'input_type':'password'
                }
            }
        }

    def create(self,validated_data):
        """Create and return a new user profile"""
        user=models.UserProfile.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user



