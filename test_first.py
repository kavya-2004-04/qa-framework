import time
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_open_site():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com")
    assert "Swag Labs" in driver.title
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    assert "inventory" in driver.current_url
    time.sleep(5)
    driver.quit()