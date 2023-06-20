from rest_framework import viewsets

from .serializers import DonationSerializer
from .models import Donation


class DonationViewSet(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()
