from pages.base_page import BasePage
from data import TestData
from locators.locators import PersonalAccountLocators
import allure

class PersonalAccountPage(BasePage):
    @allure.step('Переход в личный кабинет')
    def click_personal_account(self):
        self.click_element_with_wait(PersonalAccountLocators.PERSONAL_ACCOUNT_LINK)

    @allure.step('Заполнение поля email')
    def set_email(self):
        self.set_text(PersonalAccountLocators.NAME_INPUT, TestData.USER_EMAIL)

    @allure.step('Заполнение поля пароля')
    def set_password(self):
        self.set_text(PersonalAccountLocators.PASSWORD_INPUT, TestData.USER_PASSWORD)

    @allure.step('Подтверждение входа')
    def click_log_in_button(self):
        self.click_element_with_wait(PersonalAccountLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step('Проверка отображения кнопки профиля')
    def find_profile_button(self):
        return self.find_element_with_wait(PersonalAccountLocators.PROFILE_TAB)

    @allure.step('Переход в историю заказов')
    def click_history_order_button(self):
        self.click_element_with_wait(PersonalAccountLocators.ORDER_HISTORY_TAB)

    @allure.step('Выход из аккаунта')
    def click_exit_button(self):
        self.click_element_with_wait(PersonalAccountLocators.LOGOUT_BUTTON)

    @allure.step('Проверка кнопки входа')
    def find_enter_button(self):
        return self.find_element_with_wait(PersonalAccountLocators.LOGIN_SUBMIT_BUTTON)

    @allure.step('Авторизация пользователя')
    def log_in(self):
        self.click_personal_account()
        self.set_email()
        self.set_password()
        self.click_log_in_button()

    @allure.step('Получение номера последнего заказа')
    def get_last_order_number(self):
        return self.find_element_with_wait(PersonalAccountLocators.LAST_ORDER_IN_HISTORY).text

    @allure.step('Ожидание доступности личного кабинета')
    def wait_for_personal_account_button(self):
        self.wait_for_clickable_element(PersonalAccountLocators.PERSONAL_ACCOUNT_LINK)