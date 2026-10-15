from selenium.webdriver.common.by import By

class Categories:
    TITLE_NAME = ("//div[@class='category-card-module__category-card-title']")
    TITLE_NAME_FOR_SEARCH = ("@class='category-card-module__category-card-title'")
    CATEGORIES_AUTO = ("//a[contains(@href, '/feeds/auto/') and @class='categories-view-module__categories-view-card-link']")
    RECOMENDATION = ("//*[@aria-label='Галерея Рекомендуем']")
    VIDEO_IN_RECOMENDATION = ("//*[@class='wdp-grid-module__grid wdp-grid-module__grid_nowrap "
                                "wdp-grid-module__grid_inline' and @aria-label='Рекомендуем']")


class Feeds:
    FEEDS_SWIPE_CAROUSEL_RIGHT = ('//button[contains(@class, "btn-next")]')
    FEEDS_SWIPE_CAROUSEL_LEFT = ('//button[contains(@class, "btn-prev")]')
    LEFT_VIDEO_IN_CAROUSEL = ('//li[@class="wdp-video-carousel-module__slide wdp-video-carousel-module__slide--inline-position2"]')
    MID_VIDEO_IN_CAROUSEL = ('//li[@class="wdp-video-carousel-module__slide wdp-video-carousel-module__slide--inline-position3"]')
    RIGHT_VIDEO_IN_CAROUSEL = ('//li[@class="wdp-video-carousel-module__slide wdp-video-carousel-module__slide--inline-position4"]')


class UrlFeeds:
    feeds = [
        {"name": "'Новости и СМИ'", "url": "feeds/news/"},
        {"name": "'Трансляции'", "url": "feeds/stream/"},
        {"name": "'Подкасты'", "url": "feeds/podcast/"},
        {"name": "'Обучение'", "url": "feeds/education/"},
        {"name": "'Видеоигры'", "url": "feeds/games/"},
        {"name": "'Блогеры'", "url": "feeds/ugc/"},
        {"name": "'Спорт'", "url": "feeds/sport/"},
        {"name": "'Юмор'", "url": "feeds/fun/"},
        {"name": "'Интервью'", "url": "feeds/interview/"},
        {"name": "'Телеканалы'", "url": "feeds/tvchannels/"},
        {"name": "'Музыка'", "url": "feeds/music/"},
        {"name": "'Радио'", "url": "feeds/radio/"},
        {"name": "'Детям'", "url": "feeds/kids/"},
        {"name": "'Путешествия'", "url": "feeds/travel/"},
        {"name": "'Сериалы'", "url": "feeds/serials/"},
        {"name": "'Авто'", "url": "feeds/auto/"},
        {"name": "'Аниме'", "url": "feeds/anime/"},
        {"name": "'Культура'", "url": "feeds/culture/"},
        {"name": "'Лайфхаки'", "url": "feeds/lifehacks/"},
        {"name": "'Еда'", "url": "feeds/eda/"},
        {"name": "'Футбол'", "url": "feeds/football/"},
        {"name": "'Телешоу'", "url": "feeds/tv/"},
        {"name": "'Фильмы'", "url": "feeds/movies/"}
    ]