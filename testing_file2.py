
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
    formatted_from_date = striped_from_date.strftime("%a %m/%d")
    return formatted_from_date


driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
driver = wd.Chrome(executable_path=driver_path)
driver.get("https://www.momondo.com/")
wait = WebDriverWait(driver, 20)
target_leaving_city_airport = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div[1]/div[5]/div[1]/div[1]/div/div[1]/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/input")))
target_arrival_city_aiport = wait.until(EC.presence_of_element_located((By.XPATH,
                                                                        "/html/body/div[2]/div[1]/div[5]/div[1]/div[1]/div/div[1]/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/div[3]/div/div/input")))
# from_date = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[1]/div/input")))
# to_date = wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[1]/div/div[2]/div[2]/div/div/div[1]/div/div/div[1]/div/div[2]/div/input")))
# explore = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/c-wiz[2]/div/div[2]/c-wiz/div[1]/c-wiz/div[2]/div[1]/div[1]/div[2]/div/button")))

leaving_city = "Mumbai"
arrival_city = "London"

# selected_from_date = get_formated_date("From Date")
# selected_to_date = get_formated_date("To Date")


from_city_clear = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[5]/div[1]/div[1]/div/div[1]/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div/div/div/div[1]/div[2]/div")))
# to_city_clear = wait.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[1]/div[5]/div[1]/div[1]/div/div[1]/div/section[2]/div/div/div/div/div/div[1]/div[2]/div/div[3]/div/div/div/div[1]/div[2]/div")))
from_city_clear.click()
# to_city_clear.click()

target_leaving_city_airport.send_keys(leaving_city)
target_arrival_city_aiport.send_keys(arrival_city)


# target_arrival_ci

# from_date.send_keys(selected_from_date)
# to_date.send_keys(selected_to_date)
# explore.click()
time.sleep(10)



