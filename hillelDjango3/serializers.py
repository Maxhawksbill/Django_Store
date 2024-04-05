from django.contrib.auth.models import User

from rest_framework import serializers
from rest_framework.authtoken.models import Token


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user


class ObtainAuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True,
    )
    token = serializers.CharField(read_only=True)

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = User.objects.get(username=username)

            if not user.check_password(password):
                raise serializers.ValidationError('Incorrect password')

        else:
            raise serializers.ValidationError(
                'Must include "username" and "password"')

        attrs['user'] = user
        token, _ = Token.objects.get_or_create(user=user)
        token_key = token.key
        attrs['token'] = token_key
        return attrs
