import pandas as pd

arr = [1,4,2,5,3]
arr.sort()

arr_length = len(arr)
target_arr = [0] * arr_length

mid_position = (arr_length - 1) // 2
target_arr[mid_position] = arr[0]
left_wing_element_position = mid_position - 1
right_wing_element_position = mid_position + 1

for i in range(1, arr_length):
    if i % 2 == 0:
        target_arr[left_wing_element_position] = arr[i]
        left_wing_element_position -= 1
    else:
        target_arr[right_wing_element_position] = arr[i]
        right_wing_element_position += 1
print(target_arr)


# def pendulum_arrangement(arr):
#   # Find the minimum element and its index
#   min_element = min(arr)
#   min_index = arr.index(min_element)
#
#   # Initialize two empty lists for left and right halves
#   left = []
#   right = []
#
#   # Add the minimum element to the center
#   if len(arr) % 2 == 0:
#     left.append(min_element)
#   else:
#     right.append(min_element)
#
#   # Loop through remaining elements, alternating between left and right
#   for i in range(1, len(arr)):
#     current_element = arr[(min_index + i) % len(arr)]
#     if i % 2 == 0:
#       right.append(current_element)
#     else:
#       left.append(current_element)
#
#   # Combine left and right lists to form the final arrangement
#   return left + right
#
# # Example usage
# arr = [1, 3, 2, 5, 4]
# pendulum_arrangement(arr) # Output: [5, 3, 1, 2, 4]
#
# # Example with even elements
# arr = [1, 2, 3, 4, 5]
# pendulum_arrangement(arr) # Output: [3, 5, 1, 2, 4]
#
# from langchain import load
#
# model = load("summarization")
# text = "This is a long and complex sentence that needs to be summarized"
# preprocessed_text = text.lower().split()
# summary = model(preprocessed_text)
# print(f"Summary: {summary}")

#
# data = {
#     'col1': [1, 1, 1, 0],
#     'col2': [0, 2, 0, 0],
#     'col3': [0, 0, 0, 0],
#     'col4': [0, 0, 0, 1],
# }
#
# df = pd.DataFrame(data)
#
#
# columns_with_ones = df.columns[df.eq(3).any()].tolist()
# # columns_with_ones = df.columns[df.eq(1)]
# # print(df.eq(1).any())
#
# print("columns:", len(columns_with_ones))

# import pandas as pd
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import mean_squared_error, r2_score
# from sklearn.tree import DecisionTreeRegressor
# from scipy.sparse import hstack
# import joblib
#
# data_frame = pd.read_csv("pakwheels.csv")
#
# mode_of_features=data_frame["Features"].mode()[0]
# data_frame["Features"]=data_frame["Features"].fillna(mode_of_features)
# text_based_features=data_frame["Name"] + " " +data_frame["Location"] + " " + data_frame["Registered City"] + " " + data_frame["Color"] + " " + data_frame["Assembly"] + " " + data_frame["Features"]
# vectorizer=TfidfVectorizer(stop_words="english",max_features=5000)
# vectorized_text_based_features=vectorizer.fit_transform(text_based_features)
# numerical_based_features=data_frame.drop(["Name","Location","Registered City","Color","Assembly","Features","Price"],axis=1)
# combined_numerical_vectorized_text=hstack([numerical_based_features,vectorized_text_based_features])
# X=combined_numerical_vectorized_text
# Y=data_frame["Price"]
# X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=42)
# # model=DecisionTreeRegressor()
# # model.fit(X_train,Y_train)
# joblib.dump(model,"pak_wheels_price_prediction.joblib")
# # print("model has been trained")
# loaded_model=joblib.load("pak_wheels_price_prediction.joblib")
# prediction=loaded_model.predict(X_test)
# mse=mean_squared_error(Y_test,prediction)
# R2=r2_score(Y_test,prediction)
# print(mse,R2)
# # separate column are to be represented by space not comma, however in features since it is 1 column, we can separate different features by a comma
# text_based_features_a=["Suzuki Mehran VX (CNG) 2004 Rawalpindi Rawalpindi White Local ABS,AM/FM radio,Air Bags, Air Conditioning, DVD Player, Power Mirrors,  Power Windows, Alloy Rims , Immobilizer Key"]
# vectorized_text_based_features_a=vectorizer.transform(text_based_features_a)
# numerical_based_features=[2004,0,1,800,2,1]
# combined_text_vectorized_numerical=hstack([vectorized_text_based_features_a,numerical_based_features])
# predicition_A=loaded_model.predict(combined_text_vectorized_numerical)
# print(predicition_A)
# num = 6
# def fact(n):
#     if n == 1:
#         return n
#     else:
#         fact = 1
#         for i in range(n,1,-1):
#             fact = fact * i
#         return fact
# while_counter = 0
# result = []
# while while_counter<=num:
#     while_counter = while_counter + 1
#     f = fact(while_counter)
#     if f < num:
#         result.append(f)
#
# print(result)







# # Input a decimal number
# decimal_num = int(input("Enter a decimal number: "))
#
# # Initialize an empty string to store the binary representation
# binary_num = ""
#
# # Perform the binary conversion
# while decimal_num > 0:
#     remainder = decimal_num % 2
#     binary_num = str(remainder) + binary_num
#     decimal_num = decimal_num // 2
#     print(decimal_num)
#
# # Print the binary representation
# print(f"The binary representation of the decimal number is: {binary_num}")
#
#
# # import selenium.webdriver as wd
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import WebDriverWait
# # from selenium.webdriver.support import expected_conditions as EC
# # import time
# # from textblob import TextBlob
# #
# # driver_path = "C:/Users/92316/PycharmProjects/pythoncourse/chromedriver/chromedriver/chromedriver.exe"
# # driver =wd.Chrome(executable_path=driver_path)
# # driver.get("https://www.google.com/maps/@33.5993761,73.0287206,15z?entry=ttu")
# # wait = WebDriverWait(driver, 10)
# # search_box_access = wait.until(EC.presence_of_element_located((By.ID, "searchboxinput")))
# # drop_off_location = "SUPARCO"
# # search_box_access.send_keys(drop_off_location)
# # target_search_icon = wait.until(EC.element_to_be_clickable((By.ID, "searchbox-searchbutton")))
# # target_search_icon.click()
# # target_option_places = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "UaQhfb")))
# # counter = 0
# # for i in target_option_places:
# #     counter = counter + 1
# #     target_place_name = i.find_element(By.CLASS_NAME, "qBF1Pd")
# #     address_place_path = "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(
# #         counter + (counter + 1)) + "]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]"
# #     target_address_place = i.find_element(By.XPATH, address_place_path)
# #     print(target_place_name.text)
# #     print(target_address_place.text)
# # choice = int(input("choose a number for the place you want to visit"))
# # path_of_link_click = "//*[@id='QA0Szd']/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[1]/div[" + str(
# #     choice + (choice + 1)) + "]/div/a"
# # target_link_click = wait.until(EC.element_to_be_clickable((By.XPATH, path_of_link_click)))
# # target_link_click.click()
# # review_and_overview_button_access = wait.until(
# #     EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.RWPxGd button")))
# # review_and_overview_button_access[1].click()
# # time.sleep(20)
# # access_review_comments = wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "wiI7pd")))
# # counter = 0
# # polarity = 0
# # subjectivity = 0
# # for j in access_review_comments:
# #     counter = counter + 1
# #     analysis = TextBlob(j.text)
# #     print(j.text)
# #     print("polarity", analysis.sentiment.polarity, "subjectivity", analysis.sentiment.subjectivity)
# #     polarity = polarity + analysis.sentiment.polarity
# #     subjectivity = subjectivity + analysis.sentiment.subjectivity
# #     time.sleep(5)
# # average_polarity = polarity / counter
# # average_subjectivity = subjectivity / counter
# # print(average_polarity)
# # print(average_subjectivity)
# #
# # if average_polarity >= 0.3:
# #     print("its a good place")
# # elif average_polarity >= -0.3 and average_polarity < 0.3:
# #     print("its neutral")
# # elif average_polarity < 0.3:
# #     print("its a bad place")
# # if average_subjectivity >= 0.5:
# #     print("its subjective")
# # elif average_subjectivity < 0.5:
# #     print("its objective")
# # time.sleep(10)
# # review_and_overview_button_access[0].click()
# # direction_button_access = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='QA0Szd']/div/div/div[1]/div[3]/div/div[1]/div/div/div[2]/div[4]/div[1]/button")))
# # direction_button_access.click()
# # # print(len(direction_button_access))
# # starting_point_access = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "div#sbib_b input")))
# # starting_point = "Askari XI"
# # starting_point_access.send_keys(starting_point)
# # overview_button[0].click()