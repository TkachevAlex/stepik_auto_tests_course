from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем все поля, обязательные для заполнения.
    # Поверяем, что их 3 и заполняем их
    x = int(browser.find_element(By.CSS_SELECTOR, '#num1').text)
    y = int(browser.find_element(By.CSS_SELECTOR, '#num2').text)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(str(x + y))

    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()