from playwright.sync_api import expect

from locators.profile_locators import ProfileLocators
from locators.video_locators import VideLocators


class VideoPage:

    def __init__(self, page):
        self.page = page

    #Отправка комментария под видео
    def send_comment_on_video(self):
        text = "Хорошее видео, test943@"
        self.page.locator(VideLocators.TEXTAREA_COMMENTS).fill(text)
        self.page.locator(VideLocators.BUTTON_SEND_COMMENT).click()
        self.page.wait_for_timeout(700)
        comments = self.page.locator(VideLocators.BLOCK_COMMENTS).inner_text()

        # Проверяем что комментарий отправлен
        if text not in comments:
            raise AssertionError('Комментарий не добавлен')

    #Подписка с последующей проверкой добавления канала в список подписанных
    def subscribe_on_channel_and_check_in_profile(self):
        # Тап подписка
        subscribe_button = self.page.locator(VideLocators.SUBSCRIBE_BUTTON)
        subscribe_button.click()

        # Запись автора для сравнения
        author = self.page.locator(VideLocators.AUTHOR_NAME).inner_text().strip()

        # Проверка подписки
        self.page.wait_for_selector(VideLocators.SUBSCRIBE_BUTTON, timeout=10000)
        check_button = self.page.locator(VideLocators.SUBSCRIBE_BUTTON)
        expect(check_button).to_have_text("Вы подписаны")

        # Проверка наличия подписки
        self.page.locator(ProfileLocators.PROFILE).click()
        self.page.locator(ProfileLocators.PROFILE_MY_PROFILE).click()
        self.page.locator(ProfileLocators.MY_SUBSCRIPTIONS).click()
        subscribe_list = self.page.locator(ProfileLocators.MY_SUBSCRIPTIONS_LIST)
        check_subscribe = subscribe_list.all_inner_texts()

        author_found = any(author in item for item in check_subscribe)

        if not author_found:
            raise AssertionError('Автора нет в списке подписок')
