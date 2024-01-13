import io
import pytesseract
from PIL import Image, ImageOps, ImageFilter
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
driver =webdriver.Chrome(executable_path=driver_path)
driver.get("https://www.google.com/maps")
wait=WebDriverWait(driver,10)
target_search_button_for_location=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='searchboxinput']")))
drop_off_location="SUPARCO"
target_search_button_for_location.send_keys(drop_off_location)
target_button_access=wait.until(EC.presence_of_element_located((By.ID,"searchbox-searchbutton")))
target_button_access.click()
target_feasible_location_access_div=wait.until(EC.presence_of_element_located((By.XPATH,"//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]")))

child_div_elements = target_feasible_location_access_div.find_elements(By.XPATH, "./*[self::div]")
print(len(child_div_elements))
time.sleep(15)

# from textblob import TextBlob
# import urdu_nlp
# text = "یہ ایک بری کتاب ہے"
# analysis = TextBlob(text)
# print(analysis.sentiment.polarity, analysis.sentiment.subjectivity)

# Set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set up the Selenium webdriver
# driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
# driver =webdriver.Chrome(executable_path=driver_path)
# driver.get("https://www.youtube.com/watch?v=0FEpmdAia7Q")

# Scroll down to the comments section
# time.sleep(30)
# driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
# time.sleep(10)
# for i in range(100):
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#     time.sleep(1)