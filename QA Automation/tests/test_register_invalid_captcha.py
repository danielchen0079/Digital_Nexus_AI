from playwright.sync_api import Page
from pageObjects.POManager import POManager
from testData.registData import regist_data


def test_register_with_invalid_captcha(page: Page) -> None:
    po_manager = POManager(page)
    register_page = po_manager.get_register_page()

    register_page.goto_home()

    register_page.goto_register_page()

    register_page.fill_info(
        regist_data["email"],
        regist_data["username"],
        regist_data["password"],
        regist_data["captcha"],
    )

    error_locator = page.locator("#captcha_code-error")
    assert error_locator.inner_text().strip() == "验证码错误"
