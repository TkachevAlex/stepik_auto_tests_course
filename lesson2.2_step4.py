import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By



try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    elements = browser.find_elements(By.CSS_SELECTOR, '[required]')
    for element in elements[0:3]:
        element.send_keys('1')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    print(file_path)
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
    button = browser.find_element(By.TAG_NAME, "button")

    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()