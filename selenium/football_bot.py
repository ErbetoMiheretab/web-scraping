from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by  import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
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

dropdown = Select(driver.find_element(By.ID, 'country'))
dropdown.select_by_visible_text('Italy')

time.sleep(3)

WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))


matches = driver.find_elements(By.CSS_SELECTOR, 'tr.ng-scope')

date = []
home_team = []
score = []
away_team = []

# looping through the matches list
for match in matches:
    try:
        # Get all data first before appending
        date_text = match.find_element(By.CSS_SELECTOR, "td:nth-child(1)").text
        home_text = match.find_element(By.CSS_SELECTOR, "td:nth-child(3)").text
        score_text = match.find_element(By.CSS_SELECTOR, "td:nth-child(4)").text
        away_text = match.find_element(By.CSS_SELECTOR, "td:nth-child(5)").text
        
        # Only append if all data was successfully retrieved
        date.append(date_text)
        home_team.append(home_text)
        score.append(score_text)
        away_team.append(away_text)
        print(f"Processed: {home_text} vs {away_text}")
    except Exception as e:
        print(f"Error processing row: {e}")
        continue

# Verify lengths before creating DataFrame
print(f"Total rows collected: {len(date)}")
assert len(date) == len(home_team) == len(score) == len(away_team), "Data arrays have different lengths"

# Create Dataframe in Pandas and export to CSV
df = pd.DataFrame({
    "date": date,
    "home_team": home_team,
    "score": score,
    "away_team": away_team
})
df.to_csv("football_data.csv", index=False)
print(df)
