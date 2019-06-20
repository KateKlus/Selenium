from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


WebDriverWait(browser, 12).until(
    ec.text_to_be_present_in_element((By.ID, 'price'), '10000 RUR')
    )


button = browser.find_element_by_css_selector("button")
button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
answer = calc(x)

input_element = browser.find_element_by_id('answer')
input_element.send_keys(answer)

button = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

