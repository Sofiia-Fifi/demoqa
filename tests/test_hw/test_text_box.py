from pages.text_box import TextPage
import time


def test_text_box(browser):
    text_box = TextPage(browser)

    text_box.visit()
    text_box.full_name.send_keys('Иванов Сергей Петрович')
    text_box.current_address.send_keys('Город, улица, дом')
    text_box.btn_submit.click()
    time.sleep(3)
    actual_full_name = text_box.output_name.get_text()
    actual_current_address = text_box.output_current_address.get_text()

    assert actual_full_name == 'Name:Иванов Сергей Петрович'
    assert actual_current_address == 'Current Address :Город, улица, дом'
