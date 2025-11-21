from playwright.sync_api import Page
from pageObjects.POManager import POManager
from testData.duplicaInfo import duplica_info


def test_reset_password_and_verify(page: Page):
    po_manager = POManager(page)
    reset_page = po_manager.get_pwd_reset_page()

    reset_page.goto_home()

    reset_page.click_login_and_reset()

    reset_page.input_email(duplica_info["email"])

    success_locator = page.locator("span.color-success")
    assert success_locator.inner_text().strip() == duplica_info["email"]
