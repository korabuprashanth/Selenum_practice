from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

actions=ActionChains(driver)
blogs=driver.find_element(By.ID,"blogsmenu")
actions.move_to_element(blogs).perform()     #place cursor or move
time.sleep(4)
sele=driver.find_element(By.XPATH,"//a/span[text()='Selenium143']")
leftclick=actions.move_to_element(sele).perform()
time.sleep(4)
actions.click(leftclick).perform()          #lefclick  used .click
time.sleep(5)
img=driver.find_element(By.XPATH,"(//img)[2]")
actions.context_click(img).perform()               #right click use avtions.context_click()
actions.double_click(img).perform()                 #double_click

time.sleep(5)
driver.quit()

