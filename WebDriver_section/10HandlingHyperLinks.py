from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

driver=webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()
# TO get LIST OF LINKS & count
Links=driver.find_elements(By.XPATH,"(//div[@class='widget LinkList']//a)")
print(len(Links))
for link in Links:
    print(link.text)
    print(link.tag_name)
    print(link.get_attribute("href"))
'''for i in range (1,6):
    xpath_val="(//div[@class='widget LinkList']//a)["+str(i)+"]"
    driver.find_element(By.XPATH,xpath_val).click()
    time.sleep((2))
    driver.back()
    time.sleep(2)'''

time.sleep(4)
driver.quit()
