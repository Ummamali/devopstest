from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'path/to/chromedriver' with the actual path to your ChromeDriver executable
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Optional: Run Chrome in headless mode


driver = webdriver.Chrome(options=chrome_options)

# Replace 'http://yourappurl.com' with the URL of your app
driver.get('http://localhost:3000')

# Add your test logic here

element_locator = (By.ID, 'errormsg')

try:
    element = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(element_locator)
    )
    print("(PASS) Offline Mode: Error is being shown")
except Exception:
    print("(FAIL) Offline Mode: Error is not being shown")

# Close the browser window
driver.quit()
