from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

driver.get('http://localhost:3000')

try:
    add_cont_button = driver.find_element(By.ID, 'addCont')
    add_cont_button.click()

    name_input = driver.find_element(By.ID, 'nameInput')
    name_input.send_keys('usman')

    add_cont_btn = driver.find_element(By.ID, 'addContBtn')
    add_cont_btn.click()

    success_message = driver.find_element(By.ID, 'successMessage')
    
    if success_message.is_displayed():
        print("(PASS) All tasks completed.")
    else:
        print("(FAIL) Success message not displayed.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()
