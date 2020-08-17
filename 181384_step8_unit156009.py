from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

price = WebDriverWait(browser, 15).until(
        expected_conditions.text_to_be_present_in_element((By.ID, "price"), "100")
)
button = browser.find_element(By.ID, "book")
button.click()

input_value_str = browser.find_element(By.ID, "input_value")
input_value = input_value_str.text

result = calc(input_value)
print(result)

answer = browser.find_element(By.ID, "answer")
answer.send_keys(result)

submit = browser.find_element(By.CSS_SELECTOR, "[type = submit]")
submit.click()
