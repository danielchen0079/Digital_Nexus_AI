from playwright.sync_api import Page

class RegisterPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.register_link = page.locator(
            'a[href="/app.php/register?goto=/app.php/"] >> text=注册'
        )
        self.email_input = page.locator("#register_email")
        self.username_input = page.locator("#register_nickname")
        self.password_input = page.locator("#register_password")
        self.captcha_input = page.locator("#captcha_code")
        self.submit_btn = page.locator("#register-btn")

    def goto_home(self) -> None:
        """Given I login to Edusoho page（其实就是打开首页）"""
        self.page.goto("http://150.158.129.9/app.php/")

    def goto_register_page(self) -> None:
        """Given I am on register page"""
        self.page.goto("http://150.158.129.9/app.php/register?goto=/app.php/")
    def fill_info(self, email: str, username: str, password: str, captcha: str) -> None:
        """When I register with user"""
        self.email_input.fill(email)
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.captcha_input.fill(captcha)
        self.submit_btn.click()
