from razorpay import Order, Payment
from donation_system.settings import key_id, key_secret


class RazorPay:
    def __init__(self):
        self.key_id = key_id
        self.key_secret = key_secret

    def __str__(self):
        return f"{self.key_id} - {self.key_secret}"
