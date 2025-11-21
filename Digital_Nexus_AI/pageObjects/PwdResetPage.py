from playwright.sync_api import Page


class PwdResetPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.nav_login_btn = page.locator('nav ul.nav.user-nav li.hidden-xs a:has-text("登录")')
        self.pwd_reset_btn = page.locator('a[href="/app.php/password/reset"] >> text=找回密码')
        self.email_input = page.locator("#form_email")
        self.reset_btn = page.locator('#password-reset-form button:has-text("重设密码")')

    def goto_home(self) -> None:
        self.page.goto(
            "http://150.158.129.9/app.php/",
            wait_until="domcontentloaded",
            timeout=60000
        )

    def click_login_and_reset(self) -> None:
        self.nav_login_btn.click()
        self.pwd_reset_btn.click()

    def input_email(self, email: str) -> None:
        self.email_input.fill(email)
        self.reset_btn.click()
