from locators.base_locators import Accounts, SideBar
from locators.categories_locator import Categories, UrlFeeds, Feeds


class FeedsPage:
    def __init__(self, page):
        self.page = page

    #Переход на страницу Каталога
    def goto_feeds_page(self):
        self.page.goto(Accounts.URL_PROD, wait_until='domcontentloaded')
        self.page.locator(SideBar.FEEDS).click()
        self.page.wait_for_url(f"{Accounts.URL_PROD}categories/")
        self.page.wait_for_selector(Categories.TITLE_NAME)

    #Проверка рекомендаций в каталоге
    def check_recommendation_in_feeds(self):
        feeds = UrlFeeds.feeds
        for feed in feeds:
            self.page.locator(f"//div[text()={feed['name']} and {Categories.TITLE_NAME_FOR_SEARCH}]").click()
            self.page.wait_for_url(f"{Accounts.URL_PROD}{feed['url']}")
            self.page.query_selector(Categories.RECOMENDATION)
            self.page.query_selector(Categories.VIDEO_IN_RECOMENDATION)
            self.page.go_back()

    #Проверка свайпа в карусели рекомендаций
    def check_swipe_in_carousel(self):
        feeds = UrlFeeds.feeds

        for feed in feeds:
            (self.page.locator(f"//div[text()={feed['name']} and @class='category-card-module__category-card-title']")
             .click())
            self.page.wait_for_url(f"{Accounts.URL_PROD}{feed['url']}")

            # Проверяем изменение левого видео карусели при свайпе влево
            video_first_left = self.page.locator(Feeds.LEFT_VIDEO_IN_CAROUSEL).get_attribute("data-slide")
            self.page.locator(Feeds.FEEDS_SWIPE_CAROUSEL_LEFT).click()
            video_second_left = self.page.locator(Feeds.LEFT_VIDEO_IN_CAROUSEL).get_attribute("data-slide")
            assert video_first_left != video_second_left, "Видео в карусели не изменилось"
            video_mid = self.page.locator(Feeds.MID_VIDEO_IN_CAROUSEL).get_attribute("data-slide")
            assert video_first_left == video_mid, "Видео в карусели не изменилось"
            video_right_first = self.page.locator(Feeds.RIGHT_VIDEO_IN_CAROUSEL).get_attribute("data-slide")

            # Без задержки карусель не успевает измениться
            self.page.wait_for_timeout(700)

            # Проверяем изменение правого видео карусели при свайпе вправо
            self.page.locator(Feeds.FEEDS_SWIPE_CAROUSEL_RIGHT).click()
            video_mid = self.page.locator(Feeds.MID_VIDEO_IN_CAROUSEL).get_attribute("data-slide")
            video_right_second = self.page.locator(Feeds.RIGHT_VIDEO_IN_CAROUSEL).get_attribute("data-slide")
            assert video_right_first != video_right_second, "Видео в карусели не изменилось"
            assert video_right_first == video_mid, "Видео в карусели не изменилось"

            self.page.go_back()
