from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', "password"]
        extra_kwargs = {
            'password': {"write_only": True}
        }

    def create(self, validated_data):
        passwrod = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if passwrod is not None:
            instance.set_password(passwrod)
        instance.save()
        return instance

