from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(1)
time.sleep(4)
driv

#for tagname and attribute name
'''print(driver.find_element(By.ID,"ta1").tag_name)
print(driver.find_element(By.ID,"ta1").get_attribute("cols"))'''

#to forward the browser
'''driver.forward()
driver.back()'''

# screenshot
'''driver.save_screenshot("pjko.PNG")              
driver.get_screenshot_as_file("C:\\Users\\Prashanth k - 3444\\Desktop\\clickscan\\pjk.PNG")'''

# element size and location coordinate
'''siz_of_element=driver.find_element(By.NAME,"form1").size
print(siz_of_element)
print(siz_of_element.get("height"))
print(siz_of_element.get("width"))'''


#location of element
'''loc_of_element=driver.find_element(By.XPATH,"//td[text()='22']").location
print(loc_of_element)
print(loc_of_element.get("x"))
print(loc_of_element.get("y"))'''

# get both size and loaction
'''siz_and_loc_element=driver.find_element(By.NAME,"form1").rect
print(siz_and_loc_element)'''

driver.quit()