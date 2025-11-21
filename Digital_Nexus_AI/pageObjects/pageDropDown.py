from playwright.sync_api import Page    

class PageDropDown:
    def __init__(self, page: Page):
        self.page = page
        self.avatar_hover = page.locator('li.user-avatar-li.nav-hover')
        self.personal_setting = page.locator('ul.dropdown-menu a:has-text("个人设置")')

    def click_drop_down(self):
        self.avatar_hover.hover()
        self.page.wait_for_load_state("networkidle")
        self.personal_setting.click()
