from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")
    assert "inventory" in driver.current_url
def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login("standard_user", "wrong_password")
    assert "do not match" in login_page.get_error()