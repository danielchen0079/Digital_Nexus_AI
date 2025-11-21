from pathlib import Path
from playwright.sync_api import Page


class AvatarPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.avatar_hover = page.locator('li.user-avatar-li')
        self.drop_down = page.locator('a.dropdown-toggle')
        self.personal_setting = page.locator('ul.dropdown-menu a:has-text("个人设置")')
        self.avatar_setting = page.locator('a[href*="/settings/avatar"]')
        self.file_input = page.locator('input[type="file"]')
        self.upload_avatar_btn = page.locator(
            'a#upload-avatar-btn.btn.btn.btn-fat.btn-primary'
        )
        self.avatar_img = page.locator('form#settings-avatar-form img')

    def click_avatar(self) -> None:

        self.avatar_setting.wait_for(state="visible")
        self.avatar_setting.click()

    def get_avatar_src(self) -> str:
        self.avatar_img.wait_for(state="visible")
        return self.avatar_img.get_attribute("src")

    def upload_avatar(self, file_path: str) -> None:
        self.avatar_img.wait_for(state="visible")

        full_path = str(Path(file_path).expanduser().resolve())
        print(f"Uploading avatar from: {full_path}")
        assert Path(full_path).is_file(), "Avatar file does not exist!"

        self.file_input.set_input_files(full_path)

        self.upload_avatar_btn.wait_for(state="visible", timeout=5000)
        self.upload_avatar_btn.click()
