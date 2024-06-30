from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd


driver_path = "C:\chromedriver-win64\chromedriver-win64\chromedriver.exe"


url = "https://results.eci.gov.in/PcResultGenJune2024/index.htm#"


service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)

try:
  
    table = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "table"))
    )


    rows = []
    for row in table.find_elements(By.TAG_NAME, "tr"):
        cells = row.find_elements(By.TAG_NAME, "td")
        row_data = [cell.text.strip() for cell in cells]
        if any(row_data):  
            rows.append(row_data)
            print("Row data:", row_data)


    df = pd.DataFrame(rows)


    print("DataFrame:")
    print(df)


    df.to_csv("election_results.csv", index=False)
    print("CSV file 'election_results.csv' generated successfully.")

except Exception as e:
    print(f"Error occurred: {str(e)}")

finally:
    driver.quit()
