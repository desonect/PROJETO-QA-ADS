from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("https://practicetestautomation.com/practice-test-login/")

driver.implicitly_wait(1)


caixa_login = driver.find_element(by=By.ID, value="username")
caixa_senha = driver.find_element(by=By.ID, value="password")

caixa_login.send_keys("student")
caixa_senha.send_keys("Password123")

botao_login = driver.find_element(by=By.ID, value="submit")
botao_login.click()

time.sleep(15) 
driver.quit()