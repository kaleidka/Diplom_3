from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import allure

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента без ожидания')
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step('Ожидание и поиск видимого элемента')
    def find_element_with_wait(self, locator):
        self.wait_for_visibility_element(locator)
        return self.find_element(locator)

    @allure.step('Ожидание кликабельности элемента')
    def wait_for_clickable_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Ожидание появления элемента')
    def wait_for_element_located(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.presence_of_element_located(locator))

    @allure.step('Ожидание видимости элемента')
    def wait_for_visibility_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Ожидание изменения текста элемента')
    def wait_for_new_text(self, locator, template, time=5):
        return WebDriverWait(self.driver, time).until_not(expected_conditions.text_to_be_present_in_element(locator, template))

    @allure.step('Выполнение клика по элементу')
    def click_element(self, locator):
        self.find_element_with_wait(locator).click()

    @allure.step('Клик по элементу с ожиданием')
    def click_element_with_wait(self, locator):
        element = self.find_element_with_wait(locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ввод текста в поле')
    def set_text(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получение текста элемента')
    def get_text(self, locator):
        return self.wait_for_element_located(locator).text

    @allure.step('Перетаскивание элемента')
    def drag_and_drop_elements(self, locator_1, locator_2):
        draggable = self.wait_for_visibility_element(locator_1)
        droppable = self.wait_for_element_located(locator_2)
        ActionChains(self.driver).drag_and_drop(draggable, droppable).perform()

    def get_current_url(self):
        return self.driver.current_url