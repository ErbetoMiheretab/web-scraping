from bs4 import BeautifulSoup
import requests
import urllib3
import time

# Disable SSL verification warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

website ="https://schoolpay.berhanonline.et/site/schools-and-channels"

# Add verify=False to bypass SSL verification
result = requests.get(website, verify=False)
content = result.text
soup = BeautifulSoup(content, "lxml")

# pagination
pagination = soup.find("ul", class_="pagination")

pages = pagination.find_all("li")
last_page= "49"
with open("schools_list.txt", "w", encoding="utf-8") as file:
    file.write("")

print(f"Total pages to scrape: {last_page}")

for page in range(1, int(last_page) + 1):
    print(f"Scraping page {page} of {last_page}")
    time.sleep(1)
    result = requests.get(f"{website}?page={page}", verify=False)
    content = result.text
    soup = BeautifulSoup(content, "lxml")
    schools_div = soup.find("div", id="tb_site_schools_channels")
    
    if schools_div:
        schools_text = schools_div.get_text(separator='|', strip=True)
        schools_list = [
            school.strip() 
            for school in schools_text.split('|') 
            if school.strip() and not school.strip().isdigit() and len(school.strip()) > 1
        ]
        
        # Write each school to a file
        with open("schools_list.txt", "a", encoding="utf-8") as file:
            for school in schools_list:
                file.write(f"{school}\n")
    else:
        print(f"No content found on page {page}")

