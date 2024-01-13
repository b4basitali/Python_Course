from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create a new instance of the Firefox driver (or any other driver you are using)
driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(executable_path=driver_path)

# Open the website
driver.get("https://www.doordash.com/")

# Click on the XPath to show the login screen
login_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[1]/div/a[1]")))
login_button.click()

# Write email address
email_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/form/div[2]/div/div/div/div/div[2]/div/div[1]/input")))
email_input.send_keys("hacker4u@gmail.com")

# Click on the button to continue to sign in
continue_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/form/button")))
continue_button.click()

# Click on "Use password instead" button
use_password_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/form/button[2]")))
use_password_button.click()

# Insert password
password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/form/div[2]/div/div/div[2]/div/div[1]/input")))
password_input.send_keys("0rabnawaz.")

# Click on the sign in button
signin_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[1]/div/div/div/div/div[2]/div/div/form/button")))
signin_button.click()

# Wait for sign in to complete (adjust the sleep time as needed)
sleep(5)

# Open the specified URL
driver.get("https://www.doordash.com/store/mcdonald's-chicago-653561/?cursor=eyJzdG9yZV92ZXJ0aWNhbF9pZCI6bnVsbCwic2VhcmNoX2l0ZW1fY2Fyb3VzZWxfY3Vyc29yIjp7InF1ZXJ5IjoiIiwiaXRlbV9pZHMiOltdLCJzZWFyY2hfdGVybSI6IiIsInZlcnRpY2FsX2lkIjpudWxsLCJ2ZXJ0aWNhbF9uYW1lIjoiIn0sInN0b3JlX3ByaW1hcnlfdmVydGljYWxfaWRzIjpbMV0sImlzX3NpYmxpbmciOmZhbHNlLCJmb3JjZV9zdG9yZV9hdmFpbGFiaWxpdHlfdjIiOmZhbHNlfQ==&pickup=false")


# Click on "Start review"
start_review_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[1]/div[1]/div/div[4]/div/div/div/div[3]/span")))
start_review_button.click()

# Click on the button to give a star
star_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[4]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[1]/div/div[2]/div/button[1]")))
star_button.click()

# Write a review with more than 10 words
review_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[4]/div/div[2]/div/div[2]/div[1]/div[2]/div/div[2]/div[1]/div[2]/div/div/textarea")))
review_input.send_keys("This is a great place to eat!")

# Submit the review
submit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/div/div/button")))
submit_button.click()

# Wait for a few seconds
sleep(3)

# Click on the "Done" button
done_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/main/div/div[1]/div/div[4]/div/div[2]/div/div[2]/div[2]/div/div/button")))
done_button.click()

# Open the URL to logout the user
driver.get("https://identity.doordash.com/logout?client_id=1666519390426295040&redirect_url=https%3A%2F%2Fwww.doordash.com%2Fpost-logout%2F")

# Close the browser
driver.quit()
