from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # обнаружить и перевести в формулу:
    x_element = browser.find_element(By.CSS_SELECTOR, '#input_value')
    x = x_element.text
    y = calc(x)

    # найти и вписать полученное число из формулы
    input = browser.find_element(By.CSS_SELECTOR, '#answer')
    input.send_keys(y)

    # найти и выбрать чекбокс
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # найти и выбрать радиобаттон
    radio = browser.find_element(By.ID, "robotsRule")
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()
    time.sleep(2)
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
