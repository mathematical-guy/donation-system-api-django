from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import DonationSerializer, DonationDetailSerializer, DonorDonationsHistorySerializer, \
    ReceiverDonorsListSerializer
from .models import Donation


class DonationViewSet(viewsets.ModelViewSet):
    serializer_class = DonationSerializer
    queryset = Donation.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DonationDetailSerializer
        return DonationSerializer

    @action(methods=["get"], detail=False)
    def donation_history(self, request, *args, **kwargs):
        donor = request.user
        donations = donor.donor_donations.all()
        serializer = DonorDonationsHistorySerializer(donations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @action(methods=["get"], detail=False)
    def donators_list(self, request, *args, **kwargs):
        receiver = self.request
        donations = receiver.receiver_donations.all()
        return Response(ReceiverDonorsListSerializer(
            donations, many=True).data, status=status.HTTP_200_OK)
