from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tkinter import *

PATH = r"C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://covid19.saglik.gov.tr/")

driver.title

print(driver.title)

try:
    data = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.ID, "vaka_sayilari_home"))
    )
    print(data.text)

finally:
    driver.quit()
