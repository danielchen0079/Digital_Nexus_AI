from playwright.sync_api import Page
from pageObjects.POManager import POManager
from testData.credentials import valid_user


def test_login_and_logout(page: Page) -> None:
    po_manager = POManager(page)
    login_page = po_manager.get_login_page()

    login_page.goto()
    login_page.goto_login_page()
    login_page.login(valid_user["username"], valid_user["password"])

    logout_page = po_manager.get_logout_page()
    logout_page.click_logout_btn()
    logout_page.verify_logout()

    assert "login" in page.url
