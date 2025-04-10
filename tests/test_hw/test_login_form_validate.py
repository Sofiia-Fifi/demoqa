from pages.form_page import FormPage
from selenium.webdriver.common.keys import Keys
import time

def test_login_form_validation(browser):
    login_form = FormPage(browser)

    login_form.visit()

    assert login_form.first_name.get_dom_attribute('placeholder') == "First Name"
    assert login_form.last_name.get_dom_attribute('placeholder') == "Last Name"
    assert login_form.user_email.get_dom_attribute('placeholder') == "name@example.com" and login_form.user_email.get_dom_attribute('pattern')

    login_form.btn_submit.click_force()

    assert login_form.user_form.get_dom_attribute('class') == 'was-validated'


# выбор из выпадающего списка
def test_state_and_city(browser):
    state_city = FormPage(browser)

    state_city.visit()
    time.sleep(2)
    state_city.btn_state.scroll_to_element()
    state_city.btn_state.click()
    state_city.btn_NCR.click()
    time.sleep(2)

# ввод значения с клавиатуры
def test_state_and_city_2(browser):
    state_city = FormPage(browser)

    state_city.visit()
    time.sleep(2)
    state_city.btn_state.scroll_to_element()
    time.sleep(2)
    state_city.btn_state.click()
    state_city.input_state.send_keys('NCR')
    state_city.input_state.send_keys(Keys.ENTER)
    time.sleep(2)

# ввод значения через стрелку вниз
def test_state_and_city_3(browser):
    state_city = FormPage(browser)

    state_city.visit()
    time.sleep(2)
    state_city.btn_state.scroll_to_element()
    time.sleep(2)
    state_city.btn_state.click()
    state_city.input_state.send_keys(Keys.ARROW_DOWN)
    state_city.input_state.send_keys(Keys.ENTER)
    time.sleep(2)