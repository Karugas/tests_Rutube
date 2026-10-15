import pytest
from pages.profile_page import ProfilePage
from conftest import authorization_user

"""Авторизация пользователя и последующая проверка наличия аватарки"""


@pytest.mark.dev
def test_authorization_user_and_check_avatar(authorization_user):
    #Авторизация пользователя
    page = authorization_user
    # Проверка аватарки пользователя
    profile_page = ProfilePage(page)
    profile_page.check_profile_avatar()
