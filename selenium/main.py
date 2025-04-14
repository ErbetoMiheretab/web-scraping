from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


website = "https://www.adamchoi.co.uk/overs/detailed"
path = r"C:\chromedriver-win64\chromedriver.exe"
service = Service(path)
options = Options()
driver = webdriver.Chrome(service=service, options=options)
driver.get(website)

# Wait for the element to be present
WebDriverWait(driver, 15).until(
    EC.presence_of_element_located(
        (By.XPATH, '//label[@analytics-event="All matches"]')
    )
)


all_matches_button = driver.find_element(
    By.XPATH, '//label[@analytics-event="All matches"]'
)
all_matches_button.click()
time.sleep(25)

# driver.quit()
