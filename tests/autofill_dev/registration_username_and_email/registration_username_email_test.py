from framework.autofill_dev.main_page.AFMainPage import AFMainPage
from framework.autofill_dev.registration.email_and_username.flow.EmailAndUsernamePageFlows import \
    EmailAndUsernamePageFlows
from tests.autofill_dev.autofill_fixture import autofill_fixture as autofill_main_page
from tests.autofill_dev.registration_username_and_email.data.UsernameAndEmailUserProvider import \
    UsernameAndEmailUserProvider


def test_registration_form(autofill_main_page: AFMainPage) -> None:
    email_and_username_page = (autofill_main_page.header
                               .registration
                               .navigate_email_and_username())

    user_to_create = UsernameAndEmailUserProvider.get_random_user()
    registration_result_page = EmailAndUsernamePageFlows(email_and_username_page).register_user(user_to_create)

    registration_results = registration_result_page.get_registration_results()

    assert user_to_create.email in registration_results
    assert user_to_create.username in registration_results
    assert user_to_create.password in registration_results
