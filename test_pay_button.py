from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Open the website
driver = webdriver.Chrome()
driver.get("https://preview--utility-bill-blunders-project.lovable.app/")

wait = WebDriverWait(driver, 10)

try:
    # Step 2: Login
    account_input = wait.until(EC.presence_of_element_located((By.ID, "account")))
    account_input.send_keys("11223344")

    zip_input = wait.until(EC.presence_of_element_located((By.ID, "zipcode")))
    zip_input.send_keys("85001")

    sign_in_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit' and text()='Sign In']")))
    sign_in_button.click()

    # Step 3: Wait for dashboard to load
    pay_now_button = wait.until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Pay Now')]"))
    )
    pay_now_button.click()
    print("✅ Successfully clicked Pay Now")

    time.sleep(3)  # Just to observe before closing (optional)

except Exception as e:
    print("❌ Error:", e)

finally:
    driver.quit()
