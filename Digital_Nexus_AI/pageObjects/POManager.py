from typing import Optional
from playwright.sync_api import Page
from .LoginPage import LoginPage
from .AvatarPage import AvatarPage
from .pageDropDown import PageDropDown

class POManager:
    def __init__(self, page: Page) -> None:
        self.page: Page = page
        self._login_page: Optional[LoginPage] = None
        self._avatar_page: Optional[AvatarPage] = None
        self._page_drop_down: Optional[PageDropDown] = None

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
