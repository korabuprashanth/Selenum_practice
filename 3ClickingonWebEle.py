""" can use to Click on Hyper link, text box, button, check box, radio button, drop down etc"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

enter1=driver.find_element(By.ID,'ta1')
enter1.send_keys("HI")
time.sleep(2)
enter1.clear()
time.sleep(2)
enter1.send_keys("HLO")

time.sleep(3)