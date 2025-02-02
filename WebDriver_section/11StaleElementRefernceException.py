from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()


txtarea=driver.find_element(By.ID,"ta1")
txtarea.send_keys("Prashanth JK")

time.sleep(5)
driver.find_element(By.LINK_TEXT,"compendiumdev").click()
time.sleep(5)
driver.back()
txtarea1=driver.find_element(By.ID,"ta1")
txtarea1.clear()
time.sleep(3)
driver.quit()