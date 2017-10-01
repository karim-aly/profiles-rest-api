from rest_framework import serializers
from . import models

class HelloSerialzier(serializers.Serializer):
    """Serializes a name field for testing our APIView"""

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """A Serializer for our users profile objects"""

    class Meta:
        # define which model to use
        model = models.UserProfile

        # define fields that need to be serialized from the model
        fields = ('id', 'email', 'name', 'password')

        # define field serializing permissions
        extra_kwargs = {'password': {'write_only': True}}

    # overwrite the create method to encrypt the password provided
    def create(self, validated_data):
        """Create and return a new user"""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
