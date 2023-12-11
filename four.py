from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get('http://localhost:3000')

try:
    # Step 1: Click a button with id 'addFund'
    add_fund_button = driver.find_element_by_id('addFund')
    add_fund_button.click()

    # Step 2: Select the option with text 'usman' from select tag with id 'selectedCont'
    select_element = Select(driver.find_element_by_id('selectedCont'))
    select_element.select_by_visible_text('usman')

    # Step 3: Enter '300' in the input field with id 'amount'
    amount_input = driver.find_element_by_id('amount')
    amount_input.send_keys('300')

    # Step 4: Click the button with id 'addFundBtn'
    add_fund_btn = driver.find_element_by_id('addFundBtn')
    add_fund_btn.click()

    success_message_locator = (By.ID, 'successMessage')
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(success_message_locator)
    )
    print("(PASS) Fund has been added successfully")

except Exception as e:
    print("Error:", e)

finally:
    # Close the browser window
    driver.quit()
