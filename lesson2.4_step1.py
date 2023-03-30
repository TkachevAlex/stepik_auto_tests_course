# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text
import math
import time

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# browser = webdriver.Chrome()
# browser.get("http://suninjuly.github.io/wait1.html")
#
# time.sleep(1)
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# browser = webdriver.Chrome()
# # говорим WebDriver ждать все элементы в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait2.html")
#
# button = browser.find_element(By.ID, "verify")
# button.click()
# message = browser.find_element(By.ID, "verify_message")
#
# assert "successful" in message.text

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    WebDriverWait(browser, 12).until(
            EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )

    browser.find_element(By.TAG_NAME, "button").click()
    x = int(browser.find_element(By.CSS_SELECTOR, '#input_value').text)
    y = str(math.log(abs(12 * math.sin(x))))
    browser.find_element(By.CSS_SELECTOR, '#answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "#solve").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()