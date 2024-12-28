from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def join_google_meet(meeting_url, email, password):
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)

    # Log in to Google
    driver.get("https://accounts.google.com/signin")
    driver.find_element(By.ID, "identifierId").send_keys(email)
    driver.find_element(By.ID, "identifierNext").click()
    time.sleep(2)

    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.ID, "passwordNext").click()
    time.sleep(5)

    # Join Google Meet
    driver.get(meeting_url)
    time.sleep(5)

    # Mute mic and camera
    driver.find_element(By.CSS_SELECTOR, "div[aria-label='Turn off microphone']").click()
    driver.find_element(By.CSS_SELECTOR, "div[aria-label='Turn off camera']").click()

    driver.find_element(By.XPATH, "//span[text()='Join now']").click()
    print("Joined the meeting!")
    return driver
