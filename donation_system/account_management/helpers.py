from random import randint


def generate_otp_for_signup():
    return ''.join([str(randint(0, 9)) for _ in range(6)])
