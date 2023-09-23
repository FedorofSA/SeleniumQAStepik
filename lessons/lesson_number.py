import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r'C:/chromedriver/chromedriver.exe' # тут пропишите свой путь до exe-шника

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)
link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"

try:
    driver.maximize_window()
    driver.get(link1)
    # driver.set_page_load_timeout(10)
    driver.find_element(By.CLASS_NAME, "first_block .form-control.first").send_keys("Ivan")
    driver.find_element(By.CLASS_NAME, "first_block .form-control.second").send_keys("Petrov")
    driver.find_element(By.CLASS_NAME, "form-control.third").send_keys("mymail@mail.com")
    button = driver.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()
    time.sleep(1)
    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(2)
    driver.quit()
