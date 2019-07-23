import unittest
from selenium import webdriver
import time


class TestAbs(unittest.TestCase):
    def test_for_first_page(self):
        welcome_text = check_elements("http://suninjuly.github.io/registration1.html﻿")
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")

    def test_for_second_page(self):
        welcome_text = check_elements("http://suninjuly.github.io/registration2.html")
        self.assertEqual(welcome_text, "Поздравляем! Вы успешно зарегистировались!")


def check_elements(url):
    browser = webdriver.Chrome("C:\ChromeDriver\chromedriver.exe")
    browser.get(url)

    name = browser.find_element_by_xpath("//input[@placeholder='Введите имя']")
    name.send_keys("text")
    last_name = browser.find_element_by_xpath("//input[@placeholder='Введите фамилию']")
    last_name.send_keys("text")
    email = browser.find_element_by_xpath("//input[@placeholder='Введите Email']")
    email.send_keys("text")
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()
    time.sleep(1)
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    time.sleep(1)
    return welcome_text


if __name__ == "__main__":
    unittest.main()
