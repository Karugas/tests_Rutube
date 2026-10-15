from playwright.sync_api import expect
from locators.profile_locators import ProfileLocators


class ProfilePage:

    def __init__(self, page):
        self.page = page

    def check_profile_avatar(self):
        try:
            self.page.wait_for_selector(ProfileLocators.PROFILE)
            expect(self.page.locator(ProfileLocators.PROFILE)).to_be_visible()
        except AssertionError:
            raise AssertionError("У пользователя отсутствует аватарка")
