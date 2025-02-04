from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC      # when element throws exception
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains, Keys
driver=webdriver.Chrome()             # to Launch browse

driver.maximize_window()
driver.get("-------")  

#print(driver.find_element(By.CSS_SELECTOR,"table[id='table1']").get_attribute("border"))
driver.fullscreen_window()
driver.find_element(By.ID,"username").send_keys("******")
driver.find_element(By.ID,"password").send_keys("******")
time.sleep(1)
driver.find_element(By.XPATH,"//button[text()='Log in']").click()
time.sleep(1)
Admin_button=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Admin']")))
Admin_button.click()
time.sleep(2)
driver.find_element(By.XPATH,"//button[text()='Continue']").click()
time.sleep(1)
if (driver.find_element(By.XPATH,"//li[text()='Dashboard']").is_displayed):
    print("loooged in")
else:
    print("not logged")
try:
    driver.get("https://clickscan.terralogic.com/dashboard")  # Replace with the URL of your application
    Indexing_btn=WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"(//li[@class='ant-list-item'])[5]")))
    Indexing_btn.click()
    time.sleep(3)
    actins=ActionChains(driver)
    config=driver.find_element(By.XPATH,"(//span[@class='ant-menu-title-content'])[1]")
    actins.move_to_element(config).click().perform()
    time.sleep(4)
    config1=driver.find_element(By.XPATH,"(//div[@class='ant-collapse ant-collapse-icon-position-start mt-3 css-1r652yw']//span)[1]").click()
    txtarea=driver.find_element(By.XPATH,"//textarea[@class='ant-input css-1r652yw ant-input-outlined w-full resize-none']")
    actins.click_and_hold(txtarea).move_by_offset(0,40).release().perform()
    time.sleep(5)
finally:
    driver.quit()
