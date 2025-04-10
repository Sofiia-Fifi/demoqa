from pages.text_box import TextPage


def test_placeholder(browser):
    text_box = TextPage(browser)

    text_box.visit()
    assert text_box.full_name.get_dom_attribute('placeholder') == 'Full Name'