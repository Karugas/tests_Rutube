from enum import Enum
from selenium.webdriver.common.by import By


class BaseLocators():
    POPUP_LOGIN_OR_EMAIL = ('//input[@id="phone-or-email-login"]')
    POPUP_BUTTON_LOGIN_CONFIRM = ('//button[@id="submit-login-continue"]')
    POPUP_BUTTON_AUTHORIZATION = ('//button[@id="submit-login"]')
    POPUP_PASSWORD = ('//input[@id="login-password"]')
    IFRAME_AUTHORIZATION = ('//iframe[@id="snake-popup"]')
    VIDEO_ELEMENTS = ('//a[contains(@href, "video") and @class="wdp-link-module__link wdp-card-poster-module__posterWrapper"]')


class SideBar():
    FEEDS = ('//div[@class="menu-link-module__link menu-link-module__linkNarrow" and div[text()="Каталог"]]')
    CATEGORIES = ("https://rutube.ru/categories/")

class Accounts():
    LOGIN_EMAIL = ("carugax1@mail.ru")
    PASSWORD = ("leonardoo")
    URL_PROD = ('https://rutube.ru/')
    URL_DEV = ('https://rutube.dev/')

