import pytest
from pages.categories_page import FeedsPage
from conftest import open_browser


"""Проверка свайпов карусели на всех лентах"""


@pytest.mark.prod
def test_feeds_swipe_carousel(open_browser):
    # Открытие браузера
    page = open_browser
    #Открытие страницы
    feeds_page = FeedsPage(page)
    feeds_page.goto_feeds_page()
    #Проверка свайпа в карусели рекомендаций
    feeds_page.check_swipe_in_carousel()
