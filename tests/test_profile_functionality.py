from pages.profile_page import PersonalAccountPage
from data import Buttons, Urls
import allure
from pages.main_page import StartPage


@allure.suite('Проверки личного кабинета')
class TestProfileFunctionality:

    @allure.title('Переход в личный кабинет после авторизации')
    def test_profile_access_after_login(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        personal_account_page.click_personal_account()
        assert personal_account_page.find_profile_button().text == Buttons.PROFILE

    @allure.title('Доступ к истории заказов')
    def test_order_history_access(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        personal_account_page.click_personal_account()
        personal_account_page.click_history_order_button()
        assert personal_account_page.get_current_url() == f"{Urls.MAIN}{Urls.USER_ORDER_HISTORY}"

    @allure.title('Выход из учетной записи')
    def test_logout_functionality(self, driver):
        start_page = StartPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        personal_account_page.click_personal_account()
        personal_account_page.click_exit_button()
        assert personal_account_page.find_enter_button().text == Buttons.LOGIN

