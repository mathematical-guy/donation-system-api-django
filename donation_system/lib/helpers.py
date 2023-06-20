from faker import Faker
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

    def generate(self):

        users_to_be_created = []
        for i in range(self.count):
            name = self.fake.name()
            first_name, last_name = self._get_first_and_last_name_from_name(name=name)
            username = self._get_username_from_name(name=name)
            password = self.fake.password()

            data = {
                "username": username,
                "first_name": first_name,
                "last_name": last_name,
                "password": password,
            }
            if User.objects.filter(username=username).exists():
                continue
            users_to_be_created.append(User(**data))

        User.objects.bulk_create(objs=users_to_be_created, batch_size=100, ignore_conflicts=True)
