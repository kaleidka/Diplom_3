from pages.feed_page import OrderFeedPage
from pages.profile_page import PersonalAccountPage
from pages.main_page import StartPage
from data import Buttons
import allure

@allure.suite('Проверки ленты заказов')
class TestFeedFunctionality:

    @allure.title('Открытие деталей заказа через клик по карточке')
    def test_open_order_details(self, driver):
        order_feed_page = OrderFeedPage(driver)
        start_page = StartPage(driver)
        start_page.click_order_feed_button()
        order_feed_page.click_first_order()
        assert order_feed_page.find_compound_text().text == Buttons.ORDER_COMPOSITION

    @allure.title('Проверка отображения заказа пользователя в общей ленте')
    def test_user_order_in_feed(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.make_order()
        personal_account_page.click_personal_account()
        personal_account_page.click_history_order_button()
        order_number = personal_account_page.get_last_order_number()
        start_page.click_history_button()
        assert order_number in order_feed_page.get_order_numbers()

    @allure.title('Проверка увеличения счетчика "Всего заказов"')
    def test_total_orders_counter_increase(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.click_history_button()
        counter_order = order_feed_page.get_all_time_numbers_of_orders()
        start_page.click_constructor_button()
        start_page.make_order()
        start_page.click_history_button_with_wait()
        new_counter_order = order_feed_page.get_all_time_numbers_of_orders()
        assert new_counter_order > counter_order

    @allure.title('Проверка увеличения счетчика "Заказов за сегодня"')
    def test_today_orders_counter_increase(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.click_history_button()
        counter_order = order_feed_page.get_today_numbers_of_orders()
        start_page.click_constructor_button()
        start_page.make_order()
        start_page.click_history_button_with_wait()
        new_counter_order = order_feed_page.get_today_numbers_of_orders()
        assert new_counter_order > counter_order

    @allure.title('Проверка отображения заказа в разделе "В работе"')
    def test_order_in_progress_section(self, driver):
        order_feed_page = OrderFeedPage(driver)
        personal_account_page = PersonalAccountPage(driver)
        start_page = StartPage(driver)
        personal_account_page.log_in()
        start_page.wait_make_order()
        start_page.add_ingredient()
        start_page.click_confirm_order()
        order_number = order_feed_page.get_order_number_with_template()
        start_page.close_ingredient_details()
        start_page.click_history_button_with_wait()
        order_number_in_work = order_feed_page.get_order_numer_in_work_with_template()
        assert f"0{order_number}" == order_number_in_work

