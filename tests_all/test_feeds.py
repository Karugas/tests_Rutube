import pytest
from pages.categories_page import FeedsPage
from conftest import open_browser

"""Проверка наличия карусели "Рекомендуемое" в лентах"""


@pytest.mark.prod
def test_feeds(open_browser):
    #Открытие браузера
    page = open_browser
    # Переход на страницу Каталога
    feeds_page = FeedsPage(page)
    feeds_page.goto_feeds_page()
    #Проверка рекомендаций в каталоге
    feeds_page.check_recommendation_in_feeds()
