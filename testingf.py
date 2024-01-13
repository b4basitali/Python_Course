# import selenium.webdriver as wd
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# from selenium.webdriver.support.select import Select
from docx import Document
document = Document()
document.add_paragraph("Hello")
document.save("abc.docx")

# from selenium.webdriver.chrome.options import Options
#
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--window-size=1920x1080')  # Set the desired window size
# chrome_options.add_argument('--disable-gpu')  # Disable GPU acceleration
#
# driver_path= ""
# driver=wd.Chrome(chrome_options,executable_path=driver_path)
# driver.get("https://www.tppcrpg.net/login.php")
# wait=WebDriverWait(driver,10)
#
# # Logging into TPPC
# trainer_id_access=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/form/p[1]/input")))
# password_access=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/form/p[2]/input")))
# trainer_id=446474
# password="allah"
# trainer_id_access.send_keys(trainer_id)
# password_access.send_keys(password)
# log_in_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/form/p[3]/input")))
# log_in_button_access.click()
#
# #Enter the area for battle
# trainer_battle_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[4]/ul/li[21]/a")))
# trainer_battle_button_access.click()
# enter_opponent_number_access=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/form/p[3]/input[1]")))
# opponent_trainer=446458
# enter_opponent_number_access.send_keys(opponent_trainer)
# battle_trainer_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/form/p[3]/input[2]")))
# battle_trainer_button_access.click()

#battle with opponent
# opponent_life_hp=wait.until(EC.presence_of_element_located((By.XPATH,"/html/body/div[3]/div/div/div[1]/div[2]/div[3]/fieldset/div")))
# opponent_life_hp=opponent_life_hp.get_attribute("title").strip()
# opponent_life_hp=int(opponent_life_hp[0:len(opponent_life_hp)-14])














#
# parent_iteration = 1
# child_iteration = 1
# while True:
#     last_pokemon_health = 1
#     print(f'The parent iteration is {parent_iteration}')
#     while last_pokemon_health > 0:
#         print(f'The child iteration is {child_iteration}')
#         opponent_life_hp = wait.until(
#             EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[1]/div[2]/div[3]/fieldset/div")))
#                                                       # "/html/body/div[3]/div/div[1]/div[1]/div[2]/div[3]/fieldset/div"
#         opponent_life_hp = opponent_life_hp.get_attribute("title").strip()
#         opponent_life_hp = int(opponent_life_hp[0:len(opponent_life_hp) - 14])
#         # print(opponent_life_hp)
#         if opponent_life_hp > 0:
#             move_select_access = wait.until(
#                 EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[2]/span/select")))
#             # move_select_access.click()
#             select = Select(move_select_access)
#             select.select_by_index(2)
#             attack_button_access = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/span/input")))
#             attack_button_access.click()
#             time.sleep(5)
#
#         else:
#             continue_button_access = wait.until(
#                 EC.element_to_be_clickable((By.XPATH, "/html/body/div[3]/div/div/div[2]/span/input")))
#             continue_button_access.click()
#             time.sleep(5)
#         last_pokemon_health = wait.until(
#             EC.presence_of_element_located((By.XPATH, "/html/body/div[3]/div/div/div[3]/div[2]/ul/li[6]/div/div")))
#         last_pokemon_health = last_pokemon_health.get_attribute("style").strip()
#         last_pokemon_health = int(last_pokemon_health[7:len(last_pokemon_health) - 2])
#         child_iteration = child_iteration + 1
#         print(f'The last pokemon health is {last_pokemon_health}')
#         # print(f' Last pokemon health is : {last_pokemon_health}')
#     # restart_button_access=wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div/div[4]/a")))
#     # restart_button_access.click()
#     parent_iteration = parent_iteration + 1
#     restart_battle = wait.until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[3]/div/div[1]/div[4]/a")))
#     restart_battle.click()
#     # driver.get("https://www.tppcrpg.net/battle.php?Battle=Trainer&Trainer=446458#")
#     time.sleep(5)
#     choice_from_user=int(input("press 6 for ending the entire battle"))
#     if choice_from_user==6:
#         break
#     else:
#         continue
# applicant_data_view = "/html/body/form/div[3]/section[2]/section/div/div[2]/div/div/div[7]/a"
# while True:
#     for i in range(1,6):
#         print(f'Printing inner loop {i} times')
#
#     if int(input("Press 0 if you dont want to continue: ")) == 0:
#         break
#     else:
#         continue
# import selenium.webdriver as wd
# driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver.exe"
# driver = wd.Chrome(executable_path=driver_path)
#
# website_url = "https://moz.com/top500"
# driver.get(website_url)
# target_element = driver.find_elements_by_tag_name("a")
# for i in target_element:
#     link = i.get_attribute("href")
#     print(link)
# driver.quit()
#
#
# import selenium.webdriver as wd
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
#
#
# driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
# driver = wd.Chrome(executable_path=driver_path)
# website_url = "https://moz.com/top500"
# driver.get(website_url)
#
# wait = WebDriverWait(driver,10)
#
# tables = driver.find_elements(By.TAG_NAME, "table")  # Find all tables on the page
# target_table = tables[1]  # Access the second table using index 1 (0-based index)
#
# table_rows = target_table.find_elements(By.TAG_NAME, "tr")  # Find all rows within the target table
#
# for row in table_rows:
#     table_data = row.find_elements(By.TAG_NAME, "td")  # Find all cells within each row
#     if len(table_data) >= 3:  # Check if the row has at least 3 cells
#         third_cell = table_data[2]  # Access the third cell using index 2 (0-based index)
#         print(third_cell.text)  # Display the text of the third cell
#
# driver.quit()



















# Wait for all td elements to be present within the row
# td_locator = (By.XPATH, ".//td")
# td_elements = WebDriverWait(row, 10).until(EC.presence_of_all_elements_located(td_locator))

# element = wait.until(EC.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div/div[7]/div[1]/div/table/tbody[1]/tr[7]/td[2]/a")))
# Get the value of the 3rd td element
# third_td = td_elements[2]
# value = third_td.text
# print(value)
# driver.quit()
# target_element = driver.find_elements(By.TAG_NAME,"a")
# target_element = driver.find_elements(By.CLASS_NAME,"ml-2")
# countries = driver.find_elements(By.CLASS_NAME,"text-nowrap")
# path = "/html/body/main/div[2]/div/div[1]/table[1]/tbody/tr[1]/td[3]"
# target_element  = driver.find_element(By.XPATH,path)
# print(target_element.text)

# for i in range(1,11):
#     path = "/html/body/main/div[2]/div/div[1]/table[1]/tbody/tr[" + str(i) + "]/td[3]"
#     target_element  = driver.find_element(By.XPATH,path)
#     print(target_element.text)

# target_element =driver.find_element(By.XPATH,"/html/body/main/div[2]/div/div[1]/table[1]/tbody/tr[2]/td[3]")
#
#
# print(target_element.text)
# Navigate to the webpage
# count = 0
#
# for i in target_element:
#     count = count + 1
#     print(count,") ",i.text)


# Find all tr elements

# for i in countries:
#     print(i.text)

# target_element=driver.find_elements_by_tag_name()

# element is when the tag starts <> and ends </> and the body of text between them
#  i is just anchor tag



# import matplotlib.pyplot as plt

# age_groups = ["18-25", "26-35","36-45","46-55","56+"]
# attendee_count = [120,250,180,90,60]
# plt.bar(age_groups,attendee_count)
# plt.yticks(range(min(attendee_count),max(attendee_count)+1,50))
# plt.xlabel("Age groups")
# plt.ylabel("Attendee Count")
# plt.title("Attendee Demographics by Age")
# plt.show()


# total = 25000 + 35000 + 15000 + 20000 + 10000

# categories = ["Venue","Catering","Decorations ","Entertainment","Marketing"]
# budgets = [25000,35000,15000,20000,10000]
# plt.pie(budgets,labels= categories, autopct="%1.1f%%")
# plt.title("Event Budget Allocation")
# plt.show()

# attendee_ages = [22,25,28,30,35,40,44,43,23,44,33,11,22,33,44,55,65,66,50,40,32,55,44,33,23,43,45,65]
# plt.hist(attendee_ages, bins= 6, edgecolor = "black")
#
# plt.xlabel("Age")
# plt.ylabel("Frequency")
# plt.show()


# plt.subplots_adjust(left=0.1, right=0.9, bottom=0.1, top=0.9, hspace=0.5, wspace=0.5)
# # plot 1
# x = [2,5,6,7,8,10]
# y = [10,20,30,40,50,60]
#
#
# plt.subplot(1,3,1)
# plt.plot(x,y,marker = 'o', ms = 20, ls = 'dashed')
# plt.title("Data Analysis")
# plt.xlabel("X-Axis Data")
# plt.ylabel("Y Axis Data")
#
# # plot 2
# x = [2,4,6,9]
# y = [21,32,43,54]
#
#
# plt.subplot(1,3,2)
# plt.plot(x,y,marker = 'o', ms = 20, ls = 'dashed')
# plt.title("Plot 2")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
#
# plt.subplot(1,3,3)
# plt.plot(x,y,marker = 'o', ms = 20, ls = 'dashed')
# plt.title("Plot 2")
# plt.xlabel("X Axis")
# plt.ylabel("Y Axis")
# plt.show()


# while(True):
#     value = int(input("Do you want to break the loop? Type 0 to break the loop: "))
#     if(value == 0):
#         break
#     else:
#         print("Loop is Continue . . .")


#
# dict = {}
# dict["Key1"] = "Value1"
# print(dict)
# dict["key2"] = ["element1","element2"]
# print(dict)
# dict["Std1"] = {"Name":"Hasan"}
# print(dict)


# import func as f
#
# print(f.abc())
# name_list = ["Hasan","Basit","Shahriar"]
# name_dict = {
#     "student":"Hasan",
#     "teacher":"Basit",
#     "investigating_officer":"Shahriar"
# }
# dict_1 = {
#     "key":"value1"
# }
# dict_2 = {
#     "key":"value2"
# }
# dict_3 = {
#     "key":"value3",
#     "value":"This is Value of Value word key"
# }
# dict_4 = {
#     "key":"value4"
# }
# dicts =  {
#     "dict1":dict_1,
#     "dict2":dict_2,
#     'dict3':dict_3,
#     "dict4":dict_4
# }
# print(dicts["dict3"]["value"])
# dict_list = [dict_1,dict_2,dict_3,dict_4]
# print(dict_list[2]["value"])

# for i,j in name_dict.items():
#     print(i, "_____" , j)
# print(name_list[0])
# print(name_dict["student"])
# name_dict["boss"] =  "shahzada"
# print(name_dict)
# del name_dict["investigating_officer"]
# print(name_dict)

# list1 = ["I am List 1"]
# list2 = ["element1","element2"]
# list3 = ["I am List 3"]
# list4 = ["I am List 4"]
#
# dict_list = {
#     "list1":list1,
#     "list2":list2,
#     "list3":list3,
#     "list4":list4
# }
# print(dict_list["list2"][1])
