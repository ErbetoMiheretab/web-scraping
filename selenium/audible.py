from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time


#web = "https://www.audible.com/search"
web = "https://www.audible.com/charts/best?ref_pageloadid=not_applicable&plink=rjC2GMSnNFTMbVF3&pageLoadId=84vGSzmPvOQfOfOo&creativeId=7ba42fdf-1145-4990-b754-d2de428ba482&ref=a_search_t1_navTop_pl0cg1c0r0"
path = r"C:\chromedriver-win64\chromedriver.exe"
service = Service(path)
options = Options()
# options.add_argument("--headless=new")
# options.add_argument('window-size=1080x720')
driver = webdriver.Chrome(service=service, options=options)
driver.get(web)

# pagination
pagination= driver.find_element(By.XPATH, '//ul[contains(@class,"pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

book_title = []
book_author = []
book_length = []

current_page =1

while current_page <= last_page:
    time.sleep(3)
    # Wait for container to be present
    WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.CLASS_NAME, "adbl-impression-container"))
    )

    container = driver.find_element(By.CLASS_NAME, "adbl-impression-container")
    products = container.find_elements(By.CLASS_NAME, "productListItem")

    

    for product in products:
        try:
            title = product.find_element(By.CSS_SELECTOR, "h3[class*='bc-heading']").text
            author = product.find_element(By.CSS_SELECTOR, "li[class*='authorLabel']").text
            length = product.find_element(By.CSS_SELECTOR, "li[class*='runtimeLabel']").text

            book_title.append(title)
            book_author.append(author)
            book_length.append(length)
            print(f"Processing: {title}")
        except Exception as e:
            print(f"Error processing a book: {e}")

    print(f"Total books found: {len(book_title)}")  # Add print statement to verify data
    df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'length': book_length})
    print(f"Total books found: {len(df_books)}")  # Add print statement to verify data
    df_books.to_csv('books.csv', index=False)

    current_page += 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass

driver.quit()
