from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_experimental_option("useAutomationExtension", False)
chrome_options.add_argument('--disable-blink-features AutomationControlled')

# Initialize WebDriver with chrome options
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()

# Open the website
driver.get("http://tutorialsninja.com/demo/")

# Print the title of the page
print(driver.title)

# Wait for 4 seconds before quitting
time.sleep(4)

# Close the driver
driver.quit()