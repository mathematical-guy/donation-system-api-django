from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'donor',
        'receiver',
        'amount',
    )
    list_filter = ('donor', 'receiver')
    date_hierarchy = 'created_at'
    