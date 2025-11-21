from typing import Optional
from playwright.sync_api import Page
from .LoginPage import LoginPage
from .AvatarPage import AvatarPage
from .pageDropDown import PageDropDown
from .InfoPage import InfoPage
from .LogoutPage import LogoutPage
from .RegisterPage import RegisterPage
from .PwdResetPage import PwdResetPage

class POManager:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self._login_page: Optional[LoginPage] = None
        self._avatar_page: Optional[AvatarPage] = None
        self._page_drop_down: Optional[PageDropDown] = None
        self._info_page: Optional[InfoPage] = None
        self._logout_page: Optional[LogoutPage] = None
        self._register_page: Optional[RegisterPage] = None
        self._pwd_reset_page: Optional[PwdResetPage] = None

    def get_login_page(self) -> LoginPage:
        if self._login_page is None:
            self._login_page = LoginPage(self.page)
        return self._login_page

    def get_avatar_page(self) -> AvatarPage:
        if self._avatar_page is None:
            self._avatar_page = AvatarPage(self.page)
        return self._avatar_page

    def get_page_drop_down(self) -> PageDropDown:
        if self._page_drop_down is None:
            self._page_drop_down = PageDropDown(self.page)   
        return self._page_drop_down

    def get_info_page(self) -> InfoPage:
        if self._info_page is None:
            self._info_page = InfoPage(self.page)
        return self._info_page

    def get_logout_page(self) -> LogoutPage:
        if self._logout_page is None:
            self._logout_page = LogoutPage(self.page)
        return self._logout_page

    def get_register_page(self) -> RegisterPage:
        if self._register_page is None:
            self._register_page = RegisterPage(self.page)
        return self._register_page

    def get_pwd_reset_page(self) -> PwdResetPage:
        if self._pwd_reset_page is None:
            self._pwd_reset_page = PwdResetPage(self.page)
        return self._pwd_reset_page