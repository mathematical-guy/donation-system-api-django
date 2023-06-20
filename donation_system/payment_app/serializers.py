from django.contrib.auth import get_user_model
from rest_framework import serializers

from account_management.serializers import UserDetailSerializer
from .models import Donation

User = get_user_model()


class DonationSerializer(serializers.ModelSerializer):
    receiver = serializers.PrimaryKeyRelatedField(
        allow_null=False, allow_empty=False, queryset=User.objects.all())

    class Meta:
        model = Donation
        fields = ("id", "amount", "receiver", "donor")

    def validate_amount(self, amount):
        if amount < 0:
            raise serializers.ValidationError("Donation amount cannot be negative")
        return amount

    def validate(self, attrs: dict):
        request = self.context.get("request")
        donor = request.user
        receiver = attrs.get('receiver')

        if receiver == donor:
            raise serializers.ValidationError({"receiver": "Sorry! You cannot donate to yourself"})

        attrs["donor"] = donor

        return attrs


class DonationDetailSerializer(serializers.ModelSerializer):
    donor_details = serializers.SerializerMethodField()
    receiver_details = serializers.SerializerMethodField()

    class Meta:
        model = Donation
        fields = (
            "id", "donor_details", 'receiver_details'
        )

    def get_donor_details(self, donation: Donation):
        donor = donation.donor
        return UserDetailSerializer(instance=donor).data

    def get_receiver_details(self, donation: Donation):
        receiver = donation.receiver
        return UserDetailSerializer(instance=receiver).data


class DonorDonationsHistorySerializer(serializers.ModelSerializer):
    donated_at = serializers.DateTimeField(source="created_at", format="%Y-%m-%d %H:%M")
    receiver_name = serializers.SerializerMethodField()

    class Meta:
        model = Donation
        fields = ("id", "receiver", "donated_at", "receiver_name")

    def get_receiver_name(self, donation: Donation):
        first_name, last_name = "", ""
        if donation.receiver:
            first_name = donation.receiver.first_name
            last_name = donation.receiver.last_name

        return f"{first_name} {last_name}"
