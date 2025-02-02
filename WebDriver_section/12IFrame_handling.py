from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/iframe")
driver.maximize_window()
time.sleep(3)
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.XPATH,"//body[@id='tinymce']/p").clear()

time.sleep(3)
driver.quit()
