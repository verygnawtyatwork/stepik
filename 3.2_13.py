from selenium import webdriver
import unittest
import time

class TestAbs(unittest.TestCase):
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # тут указываем какой финальный текст хотим
        welcome_text_expected = "Congratulations! You have successfully registered!"
        
        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block > .form-group.first_class > .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector(".first_block > .form-group.second_class > .form-control.second")
        last_name.send_keys("Kapusta")
        email = browser.find_element_by_css_selector(".first_block > .form-group.third_class > .form-control.third")
        email.send_keys("brurururururr@google.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text_expected, welcome_text, "Should be another text")

    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        # тут указываем какой финальный текст хотим
        welcome_text_expected = "Congratulations! You have successfully registered!"
        
        # Ваш код, который заполняет обязательные поля
        first_name = browser.find_element_by_css_selector(".first_block > .form-group.first_class > .form-control.first")
        first_name.send_keys("Ivan")
        last_name = browser.find_element_by_css_selector(".first_block > .form-group.second_class > .form-control.second")
        last_name.send_keys("Kapusta")
        email = browser.find_element_by_css_selector(".first_block > .form-group.third_class > .form-control.third")
        email.send_keys("brurururururr@google.ru")
        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        self.assertEqual(welcome_text_expected, welcome_text, "Should be another text")

        
if __name__ == "__main__":
    unittest.main()