from rest_framework import serializers
from .models import Donation


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = ("amount", "receiver")

    def validate(self, attrs: dict):
        request = self.context.get("request")
        attrs["donor"] = request.user

        return attrs

