from faker import Faker
from random import randint
from django.contrib.auth import get_user_model

User = get_user_model()


class FakeDataGenerator:
    def __init__(self, count):
        self.count = count
        self.fake = Faker()

    @staticmethod
    def _get_first_and_last_name_from_name(name: str):
        return name.split(' ')[:2]

    @staticmethod
    def _get_username_from_name(name: str):
        return name.replace(' ', '_').lower()

    def _get_fake_indian_phone_number(self):
        return f'+91{self.fake.msisdn()[3:]}'

    def _generate_otp_for_signup(self):
        return ''.join([str(randint(0, 9)) for _ in range(6)])

    def generate(self):

        users_to_be_created = []
        for i in range(self.count):
            name = self.fake.name()
            first_name, last_name = self._get_first_and_last_name_from_name(name=name)
            username = self._get_username_from_name(name=name)
            password = self.fake.password()
            contact_number = self._get_fake_indian_phone_number()
            otp = self._generate_otp_for_signup()

            data = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
                "contact_number": contact_number,
                "otp": otp,
            }
            if User.objects.filter(username=username).exists():
                continue
            users_to_be_created.append(User(**data))

        User.objects.bulk_create(objs=users_to_be_created, batch_size=100, ignore_conflicts=True)
