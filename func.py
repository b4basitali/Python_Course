import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime


def get_formated_date(type_of_input):
    input_str = "Enter a " + type_of_input + " (YYYY-MM-DD): "
    from_date_input = input(input_str)
    striped_from_date = datetime.datetime.strptime(from_date_input, "%Y-%m-%d")
    formatted_from_date = striped_from_date.strftime("%a, %d %b")
    return formatted_from_date


driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
driver = wd.Chrome(executable_path=driver_path)
driver.get("https://www.google.com/travel/flights")
wait = WebDriverWait(driver, 20)
target_leaving_city_airport = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                         "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div/input")))
target_arrival_city_aiport = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                        "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[4]/div/div/div[1]/div/div/input")))
from_date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                       "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")))
to_date = wait.until(EC.presence_of_element_located((By.XPATH,
                                                     "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div/input")))
explore = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button")))

leaving_city = "Mumbai"
arrival_city = "London"

# selected_from_date = get_formated_date("From Date")
# selected_to_date = get_formated_date("To Date")

target_leaving_city_airport.clear()
target_arrival_city_aiport.clear()
from_date.clear()
to_date.clear()

target_leaving_city_airport.send_keys(leaving_city)
# time.sleep(2)  # Add a short delay to allow the suggestions to appear

target_leaving_city_airport.send_keys(Keys.ARROW_DOWN)  # Select the first suggestion
target_leaving_city_airport.send_keys(Keys.ARROW_DOWN)
target_leaving_city_airport.send_keys(Keys.ARROW_DOWN)
# target_leaving_city_airport.send_keys(Keys.ENTER)

# target_arrival_ci

# from_date.send_keys(selected_from_date)
# to_date.send_keys(selected_to_date)
# explore.click()
time.sleep(10)
