from playwright.sync_api import Page


class LogoutPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.avatar_hover = page.locator("li.user-avatar-li")
        self.logout_btn = page.locator('ul.dropdown-menu a:has-text("退出登录")')

    def click_logout_btn(self) -> None:
        self.avatar_hover.hover()
        self.page.wait_for_load_state("networkidle")
        self.logout_btn.click()

    def verify_logout(self) -> None:
        self.page.wait_for_url("**/login")
