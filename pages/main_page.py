from pages.base_page import BasePage
from locators.locators import StartPageLocators
import allure

class StartPage(BasePage):
    @allure.step('Переход в ленту заказов')
    def click_order_feed_button(self):
        self.click_element_with_wait(StartPageLocators.ORDER_FEED_LINK)

    @allure.step('Переход в конструктор бургеров')
    def click_constructor_button(self):
        self.click_element_with_wait(StartPageLocators.CONSTRUCTOR_LINK)

    @allure.step('Подтверждение заказа')
    def click_confirm_order(self):
        self.click_element_with_wait(StartPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Проверка заголовка конструктора')
    def find_create_order(self):
        return self.find_element_with_wait(StartPageLocators.BURGER_BUILDER_HEADER)

    @allure.step('Выбор ингредиента')
    def click_ingredient_button(self):
        self.click_element_with_wait(StartPageLocators.INGREDIENT_BUN)

    @allure.step('Проверка деталей ингредиента')
    def find_order_details(self):
        return self.find_element_with_wait(StartPageLocators.INGREDIENT_DETAILS_TITLE)

    @allure.step('Закрытие модального окна')
    def close_ingredient_details(self):
        self.click_element_with_wait(StartPageLocators.MODAL_CLOSE_BUTTON)

    @allure.step('Добавление ингредиента в заказ')
    def add_ingredient(self):
        return self.drag_and_drop_elements(StartPageLocators.INGREDIENT_BUN, StartPageLocators.BUN_DROP_AREA)

    @allure.step('Проверка счетчика ингредиентов')
    def check_order_count(self):
        return self.get_text(StartPageLocators.INGREDIENT_COUNTER)

    @allure.step('Проверка статуса заказа')
    def order_is_creating(self):
        return self.find_element_with_wait(StartPageLocators.ORDER_CREATION_MESSAGE)

    @allure.step('Создание тестового заказа')
    def make_order(self):
        self.add_ingredient()
        self.click_confirm_order()
        self.close_ingredient_details()

    @allure.step('Быстрый переход в ленту заказов')
    def click_history_button(self):
        self.click_element(StartPageLocators.ORDER_FEED_LINK)

    @allure.step('Переход в ленту заказов с ожиданием')
    def click_history_button_with_wait(self):
        self.click_element_with_wait(StartPageLocators.ORDER_FEED_LINK)

    @allure.step('Ожидание возможности оформить заказ')
    def wait_make_order(self):
        self.wait_for_clickable_element(StartPageLocators.PLACE_ORDER_BUTTON)

    @allure.step('Открытие формы авторизации')
    def click_enter_personal_account(self):
        self.click_element_with_wait(StartPageLocators.LOGIN_BUTTON)
