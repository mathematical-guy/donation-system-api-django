from twilio.rest import Client
from donation_system import settings

AUTH_TOKEN = settings.AUTH_TOKEN
TWILIO_PHONE_NUMBER = settings.TWILIO_PHONE_NUMBER
Account_SID = settings.Account_SID


class MessageHandler:
    def __init__(self, otp, phone_number):
        self.otp = otp
        self.phone_number = phone_number

    def send_otp_via_message(self):
        client = Client(Account_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=f'Your OTP is: {self.otp}',
            from_=f'{TWILIO_PHONE_NUMBER}',
            to=f"+91{self.phone_number}",
        )
