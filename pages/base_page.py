import random

import pytest

from locators.base_locators import BaseLocators


class BasePage:

    def __init__(self, page):
        self.page = page

    def select_random_video(self):
        self.page.wait_for_selector(BaseLocators.VIDEO_ELEMENTS, state='attached', timeout=10000)
        self.page.wait_for_timeout(700)
        video_elements = self.page.query_selector_all(BaseLocators.VIDEO_ELEMENTS)
        if not video_elements:
            pytest.fail('Видео не найдены')
        random_video = random.choice(video_elements)
        random_video.click()