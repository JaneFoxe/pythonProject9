from rest_framework.serializers import ModelSerializer

from users.models import User, Payments


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
