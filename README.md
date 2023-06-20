# Donation System APIs using Django and Django Rest Framework
Back-end APIs for a donation system

The repo includes a Django project with multiple functionalities like:
 - Login with both password and OTP by integrating with Twilio
 - Donating to User, its details
 - Donation History by the receiver and donor,
 - Half-baked Payment Gateway with RazorPay integration

There is Postman Collection attached and a management command **populate_dummy_data** to create default users.

**# -------------------------------- Environment Variables --------------------------------------------**

SECRET_KEY="YOUR SECRET KEY"
DEBUG=True


# ------------------------------ RazorPay Credentials ---------------------------------------------
key_id="YOUR RAZORPAY KEY ID"
key_secret="YOUR RAZORPAY KEY SECRET"

# --------------------------------------- Twilio Credentials ----------------------------------------
AUTH_TOKEN="YOUR TWILIO AUTH TOKEN"
TWILIO_PHONE_NUMBER="YOUR TWILIO REGISTERED CONTACT NUMBER"
Account_SID="YOUR TWILIO REGISTERED ACCOUNT SID"
