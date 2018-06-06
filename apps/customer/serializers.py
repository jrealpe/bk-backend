from rest_framework import serializers

from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'first_name',
                  'last_name', 'email', 'token')
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
        }

    def get_token(self, obj):
        token = self.context.get('token', None)
        return token
