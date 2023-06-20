from django.contrib.auth import get_user_model
from django.db import models
from lib.models import BaseModel

User = get_user_model()


class Donation(BaseModel):
    donor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="donor_donations")
    receiver = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="receiver_donations")
    amount = models.PositiveIntegerField()

