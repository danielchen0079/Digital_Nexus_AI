from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.nav_login_btn = page.locator(
            'nav ul.nav.user-nav li.hidden-xs a:has-text("登录")'
        )
        self.username_input = page.locator('#login_username')
        self.password_input = page.locator('#login_password')
        self.submit_login_btn = page.locator(
            'button.btn.btn-primary.btn-lg.btn-block.js-btn-login'
        )

    def goto(self) -> None:
        self.page.goto("http://150.158.129.9/app.php/")

    def goto_login_page(self) -> None:
        self.nav_login_btn.click()

    def login(self, username: str, password: str) -> None:
        self.page.wait_for_load_state("networkidle")
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.submit_login_btn.wait_for(state="visible")
        self.submit_login_btn.click()
