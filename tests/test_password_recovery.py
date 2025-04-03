from pages.password_recovery_page import RecoveryPasswordPage
from data import Urls
import allure
from pages.main_page import StartPage


@allure.suite('Проверки восстановления пароля')
class TestPasswordRecovery:

    @allure.title('Доступ к странице восстановления пароля')
    def test_password_recovery_page_access(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        start_page = StartPage(driver)
        start_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        assert recovery_password_page.get_current_url() == f"{Urls.MAIN}{Urls.PASSWORD_RECOVERY}"

    @allure.title('Процесс восстановления пароля с валидным email')
    def test_password_recovery_process(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        start_page = StartPage(driver)
        start_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        recovery_password_page.set_text_email_field()
        recovery_password_page.click_button_recovery()
        recovery_password_page.wait_for_save_button()
        assert recovery_password_page.get_current_url() == f"{Urls.MAIN}{Urls.PASSWORD_RESET}"

    @allure.title('Отображение пароля при клике на иконку')
    def test_password_visibility_toggle(self, driver):
        recovery_password_page = RecoveryPasswordPage(driver)
        start_page = StartPage(driver)
        start_page.click_enter_personal_account()
        recovery_password_page.click_recovery_button()
        recovery_password_page.set_text_email_field()
        recovery_password_page.click_button_recovery()
        recovery_password_page.wait_for_save_button()
        recovery_password_page.set_password()
        recovery_password_page.click_show_password()
        assert recovery_password_page.check_password()
