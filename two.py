from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Optional: Run Chrome in headless mode


driver = webdriver.Chrome(options=chrome_options)

driver.get('http://localhost:3000')

element_locator = (By.ID, 'allgood')

try:
    element = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located(element_locator)
    )
    print("(PASS) Online Mode: Feedback is being shown")
except Exception:
    print("(FAIL) Online Mode: Feedback is not being shown")

driver.quit()
