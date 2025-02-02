from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver=webdriver.Chrome()
driver.maximize_window()
'''driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")
driver.find_element(By.ID,"input-email").send_keys("amotooricap9@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("12345")
#driver.find_element(By.ID,"input-password").send_keys(Keys.ENTER)       
actions=ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()      '''        # used like Keys.Enter
driver.get("https://omayo.blogspot.com/")
Test1=driver.find_element(By.ID,"input-password")
links=driver.find_elements(By.XPATH,"//div[@id='LinkList1']//a")
for link in links:
	sctions=ActionChains(driver)
	sctions.key_down(Keys.CONTROL).pause(3).click(link).key_up(Keys.CONTROL).perform()  # can be used pause()
	
driver.save_screenshot("pjk.jpg")
driver.get_screenshot_as_file("pjk.jpg")  #both same

#to get screen shot of webelemet   
Test1.screenshot("pjk.png")      #also can use section in elemet and take ss

time.sleep(5)
driver.quit()