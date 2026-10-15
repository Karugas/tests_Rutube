import pytest
from pages.base_page import BasePage
from pages.video_page import VideoPage
from conftest import authorization_user


"""Проверка отправки комментария под видео"""


@pytest.mark.dev
def test_send_comment_on_video(authorization_user):
    #Открытие браузера
    page = authorization_user
    #Поиск и переход к видео
    base_page = BasePage(page)
    base_page.select_random_video()
    #Отправляем комментарий под видео и проверяем его наличие
    vide_page = VideoPage(page)
    vide_page.send_comment_on_video()


