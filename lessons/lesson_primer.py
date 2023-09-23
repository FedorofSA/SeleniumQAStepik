from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

path = r'C:/chromedriver/chromedriver.exe'

service = Service(executable_path=path)
driver = webdriver.Chrome(service=service)

link ='http://suninjuly.github.io/cats.html'
driver.implicitly_wait(5)
driver.get(link)

#driver.find_element(By.ID, "verify").click()

message = driver.find_element(By.ID, "button")
print(message.text)
assert "successful" in message.text