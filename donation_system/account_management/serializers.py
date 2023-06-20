from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from .messenger_client import MessageHandler

from account_management.helpers import generate_otp_for_signup

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


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )


class UserSignUpSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "password", "username", "contact_number")

    def create(self, validated_data):
        password = validated_data.pop("password")
        contact_number = validated_data.get("contact_number")
        otp = generate_otp_for_signup()

        validated_data["otp"] = otp
        user = super(UserSignUpSerializer, self).create(validated_data)
        user.set_password(password)
        user.save()

        # TODO: Celery can be used
        MessageHandler(otp=otp, phone_number=contact_number).send_otp_via_message()

        return user
