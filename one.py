from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()


driver = webdriver.Chrome(options=chrome_options)

driver.get('http://localhost:3000')


element_locator = (By.ID, 'errormsg')

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(element_locator)
    )
    print("(PASS) Offline Mode: Error is being shown")
except Exception:
    print("(FAIL) Offline Mode: Error is not being shown")

driver.quit()
