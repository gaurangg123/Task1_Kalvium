from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

driver_path = "C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"

url = "https://results.eci.gov.in/PcResultGenJune2024/ConstituencywiseS1327.htm"

service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

try:
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )

    rows_data = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text.strip() for cell in cells]

        if any(row_data):
            rows_data.append(
                ",".join(row_data)
            )  

   
    with open("constituency_results_rows.csv", "w", encoding="utf-8") as file:
        for row_data in rows_data:
            file.write(row_data + "\n")

    print(
        "CSV file 'constituency_results_rows.csv' generated successfully with rows data only."
    )

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    driver.quit()
