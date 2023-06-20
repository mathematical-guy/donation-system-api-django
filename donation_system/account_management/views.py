from django.contrib.auth import get_user_model
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from account_management.serializers import DonationReceiversListSerializer, LoginSerializer

User = get_user_model()


class UserLoginView(APIView):
    permission_classes = []

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.validated_data, status=status.HTTP_200_OK)


class DonationReceiversListView(ListAPIView):
    serializer_class = DonationReceiversListSerializer

    def get_queryset(self):
        user = self.request.user
        return User.objects.exclude(id=user.id)
