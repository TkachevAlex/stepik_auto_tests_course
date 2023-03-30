from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import Select
import math


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем все поля, обязательные для заполнения.
    # Поверяем, что их 3 и заполняем их
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = str(math.log(abs(12 * math.sin(x))))
    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("window.scrollBy(0, 100);")
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '[for="robotCheckbox"]').click()
    browser.find_element(By.CSS_SELECTOR, '[for="robotsRule"]').click()

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()