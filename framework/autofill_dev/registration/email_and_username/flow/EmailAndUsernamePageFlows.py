from framework.autofill_dev.registration.email_and_username.EmailAndUsernamePage import EmailAndUsernamePage
from framework.autofill_dev.registration.email_and_username.data.UsernameAndEmailUserModel import \
    UsernameAndEmailUserModel


class EmailAndUsernamePageFlows:

    def __init__(self, registration_page: EmailAndUsernamePage):
        self._registration_page = registration_page

    def register_user(self, user_to_create: UsernameAndEmailUserModel):
        self._registration_page.set_email(user_to_create.email)
        self._registration_page.set_username(user_to_create.username)
        self._registration_page.set_password(user_to_create.password)
        self._registration_page.set_confirm_password(user_to_create.password)

        return self._registration_page.register()

       