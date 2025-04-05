from pages.profile_page import PersonalAccountPage
from urls import Urls
from data import Buttons
import allure


@allure.suite('Проверки личного кабинета')
class TestProfileFunctionality:

    @allure.title('Переход в личный кабинет после авторизации')
    def test_profile_access_after_login(self, driver, authorized_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_personal_account()
        assert personal_account_page.find_profile_button().text == Buttons.PROFILE

    @allure.title('Доступ к истории заказов')
    def test_order_history_access(self, driver, authorized_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_personal_account()
        personal_account_page.click_history_order_button()
        assert personal_account_page.get_current_url() == f"{Urls.MAIN}{Urls.USER_ORDER_HISTORY}"

    @allure.title('Выход из учетной записи')
    def test_logout_functionality(self, driver, authorized_user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.click_personal_account()
        personal_account_page.click_exit_button()
        assert personal_account_page.find_enter_button().text == Buttons.LOGIN