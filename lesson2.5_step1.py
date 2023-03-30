import math
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, ".btn").click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = str(math.log(abs(12 * math.sin(x))))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.TAG_NAME, "button").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()