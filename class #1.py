import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from textblob import TextBlob

driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
driver =wd.Chrome(executable_path=driver_path)
driver.get("https://www.google.com/maps/@33.5993761,73.0287206,15z?entry=ttu")
wait = WebDriverWait(driver, 10)
search_box_access = wait.until(EC.presence_of_element_located((By.ID, "searchboxinput")))
drop_off_location = "SUPARCO"
search_box_access.send_keys(drop_off_location)
target_search_icon = wait.until(EC.element_to_be_clickable((By.ID, "searchbox-searchbutton")))
target_search_icon.click()
target_option_places = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "UaQhfb")))
counter = 0
for i in target_option_places:
    counter = counter + 1
    target_place_name = i.find_element(By.CLASS_NAME, "qBF1Pd")
    address_place_path = "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(
        counter + (counter + 1)) + "]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]"
    target_address_place = i.find_element(By.XPATH, address_place_path)
    print(target_place_name.text)
    print(target_address_place.text)
choice = int(input("choose a number for the place you want to visit"))
path_of_link_click = "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(
    choice + (choice + 1)) + "]/div/a"
target_link_click = wait.until(EC.element_to_be_clickable((By.XPATH, path_of_link_click)))
target_link_click.click()
review_and_overview_button_access = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.RWPxGd button")))
review_and_overview_button_access[1].click()
time.sleep(20)
access_review_comments = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wiI7pd")))
counter = 0
polarity = 0
subjectivity = 0
for j in access_review_comments:
    counter = counter + 1
    analysis = TextBlob(j.text)
    print(j.text)
    print("polarity", analysis.sentiment.polarity, "subjectivity", analysis.sentiment.subjectivity)
    polarity = polarity + analysis.sentiment.polarity
    subjectivity = subjectivity + analysis.sentiment.subjectivity
    time.sleep(5)
average_polarity = polarity / counter
average_subjectivity = subjectivity / counter
print(average_polarity)
print(average_subjectivity)

if average_polarity >= 0.3:
    print("its a good place")
elif average_polarity >= -0.3 and average_polarity < 0.3:
    print("its neutral")
elif average_polarity < 0.3:
    print("its a bad place")
if average_subjectivity >= 0.5:
    print("its subjective")
elif average_subjectivity < 0.5:
    print("its objective")
time.sleep(10)
review_and_overview_button_access[0].click()
direction_button_access = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[4]/div[1]/button")))
direction_button_access.click()
# print(len(direction_button_access))
starting_point_access = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#sbib_b input")))
starting_point = "Askari XI"
starting_point_access.send_keys(starting_point)
overview_button[0].click()