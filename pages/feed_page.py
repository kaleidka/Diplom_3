from pages.base_page import BasePage
from locators.locators import OrderFeedLocators
import allure

class OrderFeedPage(BasePage):
    @allure.step('Открытие деталей первого заказа')
    def click_first_order(self):
        self.click_element_with_wait(OrderFeedLocators.FIRST_ORDER_IN_LIST)

    @allure.step('Проверка отображения состава заказа')
    def find_compound_text(self):
        return self.find_element_with_wait(OrderFeedLocators.ORDER_COMPOSITION_TITLE)

    @allure.step('Получение списка номеров заказов')
    def get_order_numbers(self):
        return self.find_element_with_wait(OrderFeedLocators.ALL_ORDER_NUMBERS).text

    @allure.step('Получение общего количества заказов')
    def get_all_time_numbers_of_orders(self):
        return self.get_text(OrderFeedLocators.TOTAL_ORDERS_COUNTER)

    @allure.step('Получение количества заказов за сегодня')
    def get_today_numbers_of_orders(self):
        return self.get_text(OrderFeedLocators.TODAY_ORDERS_COUNTER)

    @allure.step('Получение номера созданного заказа')
    def get_order_number_with_template(self):
        self.wait_for_element_located(OrderFeedLocators.ORDER_NUMBER_MODAL)
        self.wait_for_new_text(OrderFeedLocators.ORDER_NUMBER_MODAL, "9999")
        return self.get_text(OrderFeedLocators.ORDER_NUMBER_MODAL)

    @allure.step('Получение номера заказа в работе')
    def get_order_numer_in_work_with_template(self):
        self.wait_for_element_located(OrderFeedLocators.ORDERS_IN_PROGRESS)
        self.wait_for_new_text(OrderFeedLocators.ORDERS_IN_PROGRESS, "Все текущие заказы готовы!")
        return self.get_text(OrderFeedLocators.ORDERS_IN_PROGRESS)