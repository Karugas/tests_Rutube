import config
import pytest
from playwright.sync_api import Playwright, sync_playwright, expect, Dialog
from locators.base_locators import BaseLocators, Accounts
from locators.video_locators import VideLocators
from locators.profile_locators import ProfileLocators

@pytest.fixture()
def jwt_profile_dev():
    request = winky.HTTPMessage('{"username":"carugax1@mail.ru","password":"leonardoo"}')
    request.headers["Content-Type"] = "application/json"
    response = request.post(config.rutube_host_dev, config.rutube_port_dev, "/multipass/api/accounts/login/")
    return response.cookies["jwt"].value

@pytest.fixture()
def jwt_profile():
    request = winky.HTTPMessage('{"username":"carugax1@mail.ru","password":"leonardoo"}')
    request.headers["Content-Type"] = "application/json"
    response = request.post(config.rutube_host, config.rutube_port, "/multipass/api/accounts/login/")
    return response.cookies["jwt"].value




"""Выбор браузера для теста + авторизация пользователя (URL_DEV)"""
@pytest.fixture(scope='function')
def authorization_user(playwright, page, browser_name = 'chromium'):
    if browser_name.lower() == 'firefox':
        browser = playwright.firefox.launch(headless=False)
    elif browser_name.lower() == 'chromium':
        browser = playwright.chromium.launch(headless=False)
    else:
        raise ValueError('Unsupported browser. Please use "firefox" or "chromium"')

    context = browser.new_context()
    page = context.new_page()

    #Авторизация пользователя
    try:
        #Открытие страницы
        page.goto(Accounts.URL_DEV, wait_until='domcontentloaded')
        page.locator(ProfileLocators.AUTHORIZATION_USER_BUTTON).click()

        # Авторизация
        iframe_element = page.wait_for_selector(BaseLocators.IFRAME_AUTHORIZATION)
        iframe = iframe_element.content_frame()

        iframe.locator(BaseLocators.POPUP_LOGIN_OR_EMAIL).fill(Accounts.LOGIN_EMAIL)
        iframe.locator(BaseLocators.POPUP_BUTTON_LOGIN_CONFIRM).click()
        iframe.locator(BaseLocators.POPUP_PASSWORD).fill(Accounts.PASSWORD)
        iframe.locator(BaseLocators.POPUP_BUTTON_AUTHORIZATION).click()

        yield page

    except Exception as e:
        print(f"Ошибка авторизации: {e}")

    finally:
        pass



"""Выбор браузера для теста (PROD)"""
@pytest.fixture(scope='function')
def open_browser(playwright, page, browser_name = 'chromium'):
    if browser_name.lower() == 'firefox':
        browser = playwright.firefox.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
    elif browser_name.lower() == 'chromium':
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
    else:
        raise ValueError('Unsupported browser. Please use "firefox" or "chromium"')