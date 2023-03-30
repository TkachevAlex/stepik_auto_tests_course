from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ищем все поля, обязательные для заполнения.
    # Поверяем, что их 3 и заполняем их
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, "[for='robotsRule']").click()
    browser.find_element(By.CSS_SELECTOR, '.btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()