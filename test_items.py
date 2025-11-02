from selenium.webdriver.common.by import By
import time  # ← добавить эту строку


def test_add_to_basket_button_is_present(browser):
    # Открываем страницу товара
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")

    # Для визуальной проверки - РАСКОММЕНТИРУЙ на время тестирования
    time.sleep(4)  # ← раскомментировать эту строку

    # Проверяем наличие кнопки добавления в корзину
    add_to_basket_button = browser.find_elements(By.CSS_SELECTOR, "button.btn-add-to-basket")

    # Убеждаемся, что кнопка существует
    assert len(add_to_basket_button) > 0, "Add to basket button is not found on the page"
