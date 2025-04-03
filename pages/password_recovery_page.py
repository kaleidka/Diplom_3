from pages.base_page import BasePage
from locators.locators import RecoveryPasswordLocators
from data import TestData
import allure

class RecoveryPasswordPage(BasePage):
    @allure.step('Инициация восстановления пароля')
    def click_recovery_button(self):
        self.click_element_with_wait(RecoveryPasswordLocators.RECOVER_PASSWORD_LINK)

    @allure.step('Ввод email для восстановления')
    def set_text_email_field(self):
        self.set_text(RecoveryPasswordLocators.EMAIL_INPUT, TestData.USER_EMAIL)

    @allure.step('Подтверждение восстановления')
    def click_button_recovery(self):
        self.click_element_with_wait(RecoveryPasswordLocators.RECOVER_BUTTON)

    @allure.step('Ожидание формы сброса пароля')
    def wait_for_save_button(self):
        self.find_element_with_wait(RecoveryPasswordLocators.SAVE_BUTTON)

    @allure.step('Ввод нового пароля')
    def set_password(self):
        self.set_text(RecoveryPasswordLocators.NEW_PASSWORD_INPUT, TestData.USER_PASSWORD)

    @allure.step('Переключение видимости пароля')
    def click_show_password(self):
        self.click_element(RecoveryPasswordLocators.SHOW_PASSWORD_ICON)

    @allure.step('Проверка активности поля пароля')
    def check_password(self):
        return self.wait_for_visibility_element(RecoveryPasswordLocators.ACTIVE_PASSWORD_FIELD)