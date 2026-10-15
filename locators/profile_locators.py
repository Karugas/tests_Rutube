class ProfileLocators:
    AUTHORIZATION_USER_BUTTON = ('//div[@class="wdp-header-auth-button-module__button" or @aria-label="Вход и регистрация"]')
    PROFILE = ('//section[@class="wdp-header-user-avatar-module__wrapper"]')
    PROFILE_MY_PROFILE = ('//span[@class="freyja_char-header-menu__text_OnVHP freyja_char-header-menu__item_ilwHA" and text()="Мой профиль"]')
    MY_SUBSCRIPTIONS = ('//a[@href="/profile/subscriptions/"]')
    MY_SUBSCRIPTIONS_LIST = ('//section[@class="wdp-settings-channel-card-module__channel"]')