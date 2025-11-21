import pytest
from playwright.sync_api import Page
from pageObjects.POManager import POManager
from testData.credentials import valid_user


def test_avatar_upload_and_verify(page: Page) -> None:
    po_manager = POManager(page)
    login_page = po_manager.get_login_page()

    login_page.goto()
    login_page.goto_login_page()
    login_page.login(valid_user["username"], valid_user["password"])

    drop_down = po_manager.get_page_drop_down()
    drop_down.click_drop_down()

    avatar_page = po_manager.get_avatar_page()
    avatar_page.click_avatar()
    old_src = avatar_page.get_avatar_src()
    print(f"Old avatar src: {old_src}")
    avatar_page.upload_avatar(valid_user["avatar_path"])
    page.wait_for_load_state("networkidle")
    new_src = avatar_page.get_avatar_src()
    print(f"New avatar src: {new_src}")

    assert new_src != old_src, "Avatar src should change after uploading new avatar"
