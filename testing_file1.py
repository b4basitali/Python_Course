import selenium.webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
driver =wd.Chrome(executable_path=driver_path)
driver.get("https://pakmcqs.com/category/pakistan-current-affairs-mcqs")
wait =WebDriverWait(driver ,10)

# header_table=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR,"header.entry-header")))
# for i in header_table:
#     target_question_strong=i.find_element(By.TAG_NAME,"strong")
#     target_question_anchor=target_question_strong.find_element(By.TAG_NAME,"a")
#     target_option_div_entry_meta=i.find_element(By.TAG_NAME,"div")
#     target_option_div_entry_content=target_option_div_entry_meta.find_element(By.TAG_NAME,"div")
#     target_option_p=target_option_div_entry_content.find_elements(By.CSS_SELECTOR,"p")
    # target_option_p=target_option_p[0].text
    # print(target_question_anchor.text)
    # print(target_option_p)
# header_table =wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR ,"header.entry-header")))

while True:
    Next_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "main#main div div a.next")))
    print("New page has been arrived")
    Next_button.click()
    time.sleep(3)

# for i in header_table:
    # target_question = i.find_element(By.CSS_SELECTOR,"strong a")
    # target_options = i.find_element(By.CSS_SELECTOR,"div div p:has(strong)")
    # target_answers = i.find_element(By.CSS_SELECTOR, "div div p:has(strong) strong")
# for i in range(1 ,len(header_table ) +1):
    # print(i)
    # path_of_question ="/html/body/div[2]/div[2]/section/main/article[" + str(i) + "]/header/strong/a"
    # path_of_question = "//*[@id='main']/article[" + str(i) + "]/header/strong/a"
    # path_of_options ="//*[@id='main']/article[" +str(i) + "]/header/div/div/p[1]"
    # path_of_answers = "//*[@id='main']/article[" + str(i) + "]/header/div/div/p[1]/strong"

    # target_question = wait.until(EC.presence_of_element_located((By.XPATH, path_of_question)))
    # target_options = wait.until(EC.presence_of_element_located((By.XPATH, path_of_options)))
    # target_answers = wait.until(EC.presence_of_element_located((By.XPATH, path_of_answers)))
    # print("_________________QUESTION_____________")
    # print(target_question.text)
    # print("____________________________________")
    # print(target_options.text)
    # print("_________________ANSWER_____________")
    # print(target_answers.text)
    # print("____________________________________")
# import datetime
#
# date_input = input("Enter a date (YYYY-MM-DD): ")
# date = datetime.datetime.strptime(date_input, "%Y-%m-%d")
#
# formatted_date = date.strftime("%a %m/%d")
# print("Formatted date:", formatted_date)


# from tkinter import ttk
# from tkcalendar import Calendar
#
# def get_selected_date():
#     selected_date = cal.selection_get()
#     print("Selected date:", selected_date)
#
# root = tk.Tk()
# root.title("Date Input")
#
# cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
# cal.pack()
#
# select_button = ttk.Button(root, text="Select", command=get_selected_date)
# select_button.pack()
#
# root.mainloop()
