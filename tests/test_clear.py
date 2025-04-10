from pages.text_box import TextPage
import time


def test_clear(browser):
    text_box = TextPage(browser)

    text_box.visit()
    text_box.full_name.send_keys('Здесь могла быть ваша реклама')
    time.sleep(2)
    text_box.full_name.clear()
    time.sleep(2)

    assert text_box.full_name.get_text() == ''