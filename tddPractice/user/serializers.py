from rest_framework import serializers

from modelsTdd import models

class UserRegistrationSerializer(serializers.ModelSerializer):
    """Handling serialization of user registration"""
    class Meta:
        model = models.UserProfile
        fields = ("id", "email", "name", "surname", "password")
        extra_kwargs = {
            "password":{
                "write_only":True,
                "style":{"input_type":"password"}
            }
        }

    def create(self, validated_data):
        """Tells the serializer how to create a user"""
        user = models.UserProfile.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        """Handle updating user account"""
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)

        return super().update(instance, validated_data)

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializer for viewing user profile"""

    class Meta:
        model = models.UserProfile
        fields=["id","name", "surname", "email"]