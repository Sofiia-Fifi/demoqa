from pages.accordian_page import Accordion
import time


def test_visible_accordion(browser):
    accordian_page = Accordion(browser)

    accordian_page.visit()
    assert accordian_page.section_1_content.visible()
    accordian_page.btn_section_1_card_header.click()
    time.sleep(2)
    assert not accordian_page.section_1_content.visible()

def test_visible_accordion_default(browser):
    accordian_page = Accordion(browser)

    accordian_page.visit()
    assert not accordian_page.section_2_content_1.visible()
    assert not accordian_page.section_2_content_2.visible()
    assert not accordian_page.section_3_content.visible()
