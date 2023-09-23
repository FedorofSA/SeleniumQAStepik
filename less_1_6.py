import time
#import math
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
text = '224592'#str(math.ceil(math.pow(math.pi, math.e)*10000))
path = r'C:/chromedriver/chromedriver.exe'

link = "http://suninjuly.github.io/simple_form_find_task.html"
link1 = "http://suninjuly.github.io/find_link_text"
s = Service(executable_path=path)
driver = webdriver.Chrome(service=s)

try:
    driver.maximize_window()
    driver.get(link1)
    link2 = driver.find_element(By.LINK_TEXT, text)
    link2.click()
    #driver.get(link)
    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "form-control.city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()