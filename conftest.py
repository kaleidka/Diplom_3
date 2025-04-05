import pytest
from selenium import webdriver
from urls import Urls
from pages.main_page import StartPage
from pages.profile_page import PersonalAccountPage


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = webdriver
    if request.param == 'chrome':
        driver = webdriver.Chrome()
        driver.get(Urls.MAIN)
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.get(Urls.MAIN)
    yield driver
    driver.quit()

@pytest.fixture
def authorized_user(driver):
    personal_account_page = PersonalAccountPage(driver)
    start_page = StartPage(driver)
    personal_account_page.log_in()
    start_page.wait_make_order()
    yield driver
