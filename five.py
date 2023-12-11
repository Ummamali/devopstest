from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('http://localhost:3000')

try:
    div_element_locator = (By.CLASS_NAME, 'output')
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(div_element_locator)
    )

    p_usman = div_element.find_element(By.XPATH, './/p[contains(text(), "usman")]')
    p_300 = div_element.find_element(By.XPATH, './/p[contains(text(), "300")]')
    delete_button = div_element.find_element(By.XPATH, './/button[contains(text(), "delete")]')

    print("(PASS) Fund added is listed on the screen!")

except Exception as e:
    print("Error:", e)

finally:
    driver.quit()
