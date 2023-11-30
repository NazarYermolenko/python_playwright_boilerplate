from faker import Faker

from framework.autofill_dev.registration.email_and_username.data.UsernameAndEmailUserModel import \
    UsernameAndEmailUserModel


class UsernameAndEmailUserProvider:

    @staticmethod
    def get_random_user() -> UsernameAndEmailUserModel:
        fake = Faker()
        return UsernameAndEmailUserModel(email=fake.email(), username=fake.user_name(), password=fake.password())

