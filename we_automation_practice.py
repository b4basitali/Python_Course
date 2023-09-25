import io
import pytesseract
from PIL import Image, ImageOps, ImageFilter
import numpy as np
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from skimage import morphology, filters
import time
from textblob import TextBlob
# analysis = TextBlob("i love this video")
# print(analysis.sentiment.polarity, analysis.sentiment.subjectivity)

# Set the path to the Tesseract executable
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Set up the Selenium webdriver
driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
driver =webdriver.Chrome(executable_path=driver_path)
#
# # Navigate to the webpage with the captcha
# driver.get("https://www.daewoo.com.pk/")
#
# # Locate and capture the captcha image
# wait = WebDriverWait(driver, 20)
# time.sleep(10)
# captcha_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "img#CaptchaImage")))
#
# # captcha_element = driver.find_element(By.CSS_SELECTOR, "img#CaptchaImage")
# print("Captcha element:", captcha_element)
# captcha_image = captcha_element.screenshot_as_png
#
# # Process the captcha image
# captcha_image = Image.open(io.BytesIO(captcha_image))
# # Convert the image to grayscale
# captcha_image = captcha_image.convert("L")
# #
# # # Apply thresholding to enhance contrast
# threshold_value = 140
# captcha_image = captcha_image.point(lambda p: p > threshold_value and 255)
#
# # Convert the PIL image to a NumPy array
# captcha_array = np.array(captcha_image)
#
# # Apply erosion
# captcha_array = morphology.erosion(captcha_array)
#
# # Apply dilation
# captcha_array = morphology.dilation(captcha_array)
#
# # Convert the NumPy array back to a PIL image
# captcha_image = Image.fromarray(captcha_array)
#
# # Apply noise reduction using a Gaussian filter
# captcha_image = captcha_image.filter(ImageFilter.GaussianBlur(radius=1))
#
# captcha_image.save("preprocessed_captcha.png")
# captcha_text = pytesseract.image_to_string(captcha_image)
#
# # Close the browser
# # driver.quit()
#
# # Display the captcha text
# print("Captcha Text:", captcha_text)
#
#


# Go to the YouTube video page
driver.get("https://www.youtube.com/watch?v=0FEpmdAia7Q")

# Scroll down to the comments section
for i in range(100):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)

# Get the comments
wait = WebDriverWait(driver, 20)
# time.sleep(10)
comments = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "ytd-comment-thread-renderer")))
#
#
#
for comment in comments:
    text = wait.until(EC.presence_of_element_located((By.ID, "content-text")))
    print(text.text)
    # analysis = TextBlob(text)
    # print(analysis.sentiment.polarity, analysis.sentiment.subjectivity)

# Close the web driver
driver.quit()# Go to the YouTube video page
# driver.get("https://www.youtube.com/watch?v=video_id")

# Get the comments
# comments = driver.find_elements_by_class_name("ytd-comment-renderer")

# Analyze the text and emotions of the comments
# for comment in comments:
#     text = comment.find_element_by_id("content-text").text
#     analysis = TextBlob(text)
#     print(analysis.sentiment.polarity, analysis.sentiment.subjectivity)

# Close the web driver
# driver.quit()