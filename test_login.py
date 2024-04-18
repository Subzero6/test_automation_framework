import pytest
from pages.login_page import LoginPage

@pytest.mark.parametrize('username, password', [('user1', 'pass1'), ('user2', 'pass2')])
def test_login(username, password):
    login_page = LoginPage()
    login_page.open()
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login_button()
    assert login_page.is_login_successful()