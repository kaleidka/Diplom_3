from selenium.webdriver.common.by import By

class StartPageLocators:
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти в аккаунт']")
    ORDER_FEED_LINK = (By.XPATH, ".//p[text()='Лента Заказов']")
    CONSTRUCTOR_LINK = (By.XPATH, ".//p[text()='Конструктор']")
    BURGER_BUILDER_HEADER = (By.XPATH, ".//h1[text()='Соберите бургер']")
    INGREDIENT_BUN = (By.XPATH, ".//p[text()='Краторная булка N-200i']")
    INGREDIENT_DETAILS_TITLE = (By.XPATH, ".//h2[text()='Детали ингредиента']")
    MODAL_CLOSE_BUTTON = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    BUN_DROP_AREA = (By.XPATH, './/*[text()="Перетяните булочку сюда (низ)"]')
    INGREDIENT_COUNTER = (By.XPATH, ".//*[@class ='counter_counter__num__3nue1'and text()='2']")
    PLACE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    ORDER_CREATION_MESSAGE = (By.XPATH, ".//p[text()='Ваш заказ начали готовить']")

class RecoveryPasswordLocators:
    RECOVER_BUTTON = (By.XPATH, ".//button[text()='Восстановить']")
    EMAIL_INPUT = (By.XPATH, ".//input[@type='text']")
    NEW_PASSWORD_INPUT = (By.XPATH, ".//input[@name='Введите новый пароль']")
    SHOW_PASSWORD_ICON = (By.XPATH, ".//div[@class='input__icon input__icon-action']")
    ACTIVE_PASSWORD_FIELD = (By.CSS_SELECTOR, '.input.input_status_active')
    SAVE_BUTTON = (By.XPATH, ".//button[text()='Сохранить']")
    RECOVER_PASSWORD_LINK = (By.XPATH, ".//a[text()='Восстановить пароль']")

class PersonalAccountLocators:
    PROFILE_TAB = (By.XPATH, ".//a[text()='Профиль']")
    ORDER_HISTORY_TAB = (By.XPATH, ".//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, ".//button[text()='Выход']")
    LAST_ORDER_IN_HISTORY = (By.XPATH, './/li[last()]/a[contains(@href, "order-history")]/*/p[1]')
    PERSONAL_ACCOUNT_LINK = (By.XPATH, ".//p[text()='Личный Кабинет']")
    NAME_INPUT = (By.XPATH, ".//input[@name='name']")
    PASSWORD_INPUT = (By.XPATH, ".//input[@name='Пароль']")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")

class OrderFeedLocators:
    FIRST_ORDER_IN_LIST = (By.XPATH, './/*[contains(@class, "OrderHistory_link")]')
    ORDER_COMPOSITION_TITLE = (By.XPATH, ".//p[text()='Cостав']")
    ALL_ORDER_NUMBERS = (By.XPATH, './/ul[contains(@class,"OrderFeed_list")]//p[contains(text(),"#")]')
    TOTAL_ORDERS_COUNTER = (By.XPATH, './/p[text()="Выполнено за все время:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
    TODAY_ORDERS_COUNTER = (By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p[contains(@class,"OrderFeed_number")]')
    ORDER_NUMBER_MODAL = (By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text ""text_type_digits-large mb-8']")
    ORDERS_IN_PROGRESS = (By.XPATH, ".//ul[contains(@class, 'ListReady')]/li")