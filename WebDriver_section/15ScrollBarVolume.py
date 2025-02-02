
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/p/page3.html")

bar=driver.find_element(By.XPATH,"(//div/a[@class='ui-slider-handle ui-btn ui-shadow ui-btn-null'])[1]")

actions=ActionChains(driver)
actions.drag_and_drop_by_offset(bar,100,0).perform()
time.sleep(7)
driver.quit()