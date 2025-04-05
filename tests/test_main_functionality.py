from pages.profile_page import PersonalAccountPage
from pages.main_page import StartPage
from data import Buttons
from urls import Urls
import allure

@allure.suite('Проверки основного функционала')
class TestMainFunctionality:

    @allure.title('Переход в раздел конструктора из ленты заказов')
    def test_transition_constructor(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        start_page.click_order_feed_button()
        personal_account_page.wait_for_personal_account_button()
        start_page.click_constructor_button()
        assert start_page.find_create_order().is_displayed()

    @allure.title('Переход в ленту заказов с главной страницы')
    def test_transition_order_feed(self, driver):
        start_page = StartPage(driver)
        start_page.click_order_feed_button()
        assert start_page.get_current_url() == f"{Urls.MAIN}{Urls.ORDERS_FEED}"

    @allure.title('Отображение модального окна с деталями ингредиента')
    def test_click_ingredient(self, driver):
        start_page = StartPage(driver)
        start_page.click_ingredient_button()
        assert start_page.find_order_details().text == Buttons.INGREDIENT_DETAILS

    @allure.title('Закрытие модального окна с деталями ингредиента')
    def test_close_order_details(self, driver):
        start_page = StartPage(driver)
        start_page.click_ingredient_button()
        start_page.close_ingredient_details()
        assert start_page.find_create_order().is_displayed()

    @allure.title('Изменение счетчика при добавлении ингредиента')
    def test_add_ingredient_in_order(self, driver):
        start_page = StartPage(driver)
        start_page.add_ingredient()
        assert start_page.check_order_count() == '2'

    @allure.title('Оформление заказа авторизованным пользователем')
    def test_authorized_order_creation(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.add_ingredient()
        start_page.click_confirm_order()
        assert start_page.order_is_creating().text == Buttons.ORDER_IN_PROGRESS

