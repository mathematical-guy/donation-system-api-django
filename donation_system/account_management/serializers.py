from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers

User = get_user_model()


class DonationReceiversListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name",)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User

    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExists:
            raise serializers.ValidationError({"username": "User with this username is not registered"})

        if not user.check_password(raw_password=password):
            raise serializers.ValidationError("Invalid Credentials")

        token, created = Token.objects.get_or_create(user=user)
        attrs["token"] = token.key

        return attrs
