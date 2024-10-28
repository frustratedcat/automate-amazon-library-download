from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()

driver.get("https://wwww.amazon.com")

# driver.implicitly_wait(5)

click_sign_in = driver.find_element(By.ID, "nav-link-accountList").click()

input_email = driver.find_element(By.ID, "ap_email")
input_email.send_keys("" + Keys.ENTER)

input_password = driver.find_element(By.ID, "ap_password")
input_password.send_keys("" + Keys.ENTER)

time.sleep(5)

driver.quit()