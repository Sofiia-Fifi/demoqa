import time

from pages.modal_dialogs import ModalDialogs


def test_check_text_modal(browser):
    modal_page = ModalDialogs(browser)

    modal_page.visit()
    assert modal_page.btn_small_modal.exist()
    assert modal_page.btn_large_modal.exist()

    modal_page.btn_small_modal.click()
    assert modal_page.modal_dialog.exist()
    assert modal_page.btn_close_small_modal.exist()
    time.sleep(2)
    modal_page.btn_close_small_modal.click()
    assert not modal_page.modal_dialog.exist()
    time.sleep(2)

    modal_page.btn_large_modal.click()
    assert modal_page.modal_dialog.exist()
    assert modal_page.btn_close_large_modal.exist()
    time.sleep(2)
    modal_page.btn_close_large_modal.click()
    assert not modal_page.modal_dialog.exist()
    time.sleep(2)