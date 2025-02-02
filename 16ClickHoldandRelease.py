from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
box6=driver.find_element(By.XPATH,"//div[@id='box6']")
spain=driver.find_element(By.XPATH,"//div[@id='box107']")
actions=ActionChains(driver)

#actions.click_and_hold(box6).move_to_element(spain).release().perform()
actions.drag_and_drop(box6,spain).perform()
time.sleep(4)
driver.quit()