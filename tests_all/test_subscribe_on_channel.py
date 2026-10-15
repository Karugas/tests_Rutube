import pytest
from conftest import authorization_user
from pages.video_page import VideoPage
from pages.base_page import BasePage

"""Проверка добавления автора после подписки на его канал в список подписок"""


@pytest.mark.dev
def test_check_subscribe_on_channel(authorization_user):
    # Открытие браузера
    page = authorization_user
    #Поиск и переход к видео
    base_page = BasePage(page)
    base_page.select_random_video()
    #Подписка с последующей проверкой добавления канала в список подписанных
    video_page = VideoPage(page)
    video_page.subscribe_on_channel_and_check_in_profile()
