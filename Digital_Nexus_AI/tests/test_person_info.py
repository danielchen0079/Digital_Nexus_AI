from playwright.sync_api import Page
from pageObjects.POManager import POManager
from testData.credentials import valid_user
from testData.personInfo import user_info


def test_person_info_edit(page: Page):
    po_manager = POManager(page)
    login_page = po_manager.get_login_page()

    login_page.goto()
    login_page.goto_login_page()
    login_page.login(valid_user["username"], valid_user["password"])

    drop_down = po_manager.get_page_drop_down()
    drop_down.click_drop_down()

    info_page = po_manager.get_info_page()
    info_page.fill_info(
        user_info["realName"],
        user_info["sex"],
        user_info["idNum"],
        user_info["phone"],
        user_info["company"],
        user_info["job"],
        user_info["title"],
        user_info["signature"],
        user_info["intro"],
        user_info["site"],
        user_info["weibo"],
        user_info["weChat"],
        user_info["qq"],
    )
