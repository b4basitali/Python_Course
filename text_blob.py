# +++++++++++  ========================
# Step 1: Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 2: Load your dataset
# Replace 'your_data.csv' with the actual file name
df = pd.read_excel('stress.xlsx')

# Step 3: Basic data exploration
print(df.head())  # To see the first few rows of the dataset
print(df.describe())  # To get summary statistics for numerical columns
print(df.info())  # To get a summary of dataset including data types and non-null values

# Step 4: Pre-process the dataset
# Let's assume 'stress_level' is categorical (Low, Medium, High)
# and that all other columns are numerical or have been encoded as such
X = df.drop('stress_level', axis=1)
y = df['stress_level']  # Target

# Step 5: Split the data0
X_ttrain_test_split(X, y, test_size=0.3, random_state=42)

# Step 6: Feature Scaling (if necessary)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 7: Train a classification model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_scaled, y_train)

# Step 8: Evaluate the model
y_pred = model.predict(X_test_scaled)
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Step 9: Make predictions with the model
# Let's say you have a new student with the following factors: psych_factor=4, env_factor=3, social_factor=5
# Note: The values should be scaled as well since the model was trained on scaled features
new_student = scaler.transform([[12,11,13,14,13,12,5,3,1,0,6,5,4,3,5,3,2,1,0,1]])
predicted_stress_level = model.predict(new_student)
print("Predicted Stress Level:", predicted_stress_level)

# item = "a"
# list_of_item = ["a","b","c","e"]
# box = 0
# for i in list_of_item:
#     if i == item:
#         print(item, "Found")
#         box = 1
#         break
#     else:
#         box = 0
# if box == 0:
#     print(item, "Not Found")


# for i in items:
#     for j in list_of_item:
#         if i == j:
#             box = 1
#             break
#         else:
#             box = 0





# def find_substrings(binary_string):
#     substrings = []
#     i = 0
#
#     while i < len(binary_string):
#         if binary_string[i] == '1':
#             j = i + 1
#             while j < len(binary_string) and binary_string[j] == '1':
#                 substrings.append(binary_string[i:j+1])
#                 j += 1
#             i = j
#         else:
#             i += 1
#
#     return substrings
#
# binary_string = "1111"
# substrings = find_substrings(binary_string)
#
# for substring in substrings:
#     print(substring)
#


import numpy as np
import pandas as pd
# data_frame=pd.DataFrame([["Ali",1000,"23-10-2023"],["Hasan",14000,"25-10-2023"],["Basit",15000,"18-10-2023"],["Azlan",1500,"23-10-2023"],["Ali",1430,"24-10-2023"],["Hasan",13000,"26-10-2023"],["Basit",13200,"19-10-2023"],["Azlan",19000,"25-10-2023"],["Ali",51200,"25-10-2023"],["Hasan",1100,"27-10-2023"],["Basit",9870,"20-10-2023"],["Azlan",9210,"28-10-2023"]],columns=["name","expenses","date"])
# data_frame.applymap()
# expenses_by_person=data_frame.groupby("name").count()
# print(expenses_by_person)
# expenses_sum=data_frame.groupby("name").sum()
# print(expenses_sum)
# mean=data_frame.groupby("name").mean(numeric_only=True)
# print(mean)
# df = pd.DataFrame([[8639,"Basit","SPS-1","Present"],
#                          [4380,"Yasir Siddiqui","SPS-1","Not Present"],
#                          [10095,"Salman","SPS-2","Present"],
#                          [7970,"Muhammad Arif","SPS-2","Not Present"],
#                          [8287,"Awais Ali Khan","SPS-3","Present"],
#                          [5089,"Muhammad Ali","SPS-3","Not Present"],
#                          [3002,"Shahriar huda","SPS-4","Present"],
#                          [28089,"Ahmed Ghani","SPS-4","Not Present"],
#                          [1235,"Irfan Khan","SPS-5","Present"],
#                          [9897,"Imran Ali Naqi","SPS-5","Not Present"]],columns=["P#","name","Scale","Avail"])
# def get_len(x):
#     return len(x)
#
# df["len"] = df["name"].apply(get_len)
# print(df)
# df = pd.DataFrame([[8639,1000,"01-10-23","Present"],
#                          [4380,200,"01-10-23","Not Present"],
#                          [8639,2000,"01-10-23","Present"],
#                          [7970,456,"01-10-23","Not Present"],
#                          [8287,785,"01-10-23","Present"],
#                          [7970,1000,"01-10-23","Not Present"],
#                          [3002,633,"01-10-23","Present"],
#                          [4380,500,"01-10-23","Not Present"],
#                          [3002,600,"01-10-23","Present"],
#                          [8287,500,"01-10-23","Not Present"]],columns=["P#","expences","date","Avail"])
#
# df.drop("Avail",axis=1, inplace=True)
#
# gp = df.groupby("P#").sum()
# print(gp)

# df.sort_values(by="P#",inplace=True)
# print(df)











# df = pd.DataFrame([[8639,"Regular","SPS-1","Present"],
#                          [4380,"Contract","SPS-1","Not Present"],
#                          [10095,"Casual","SPS-2","Present"],
#                          [7970,"Regular","SPS-2","Not Present"],
#                          [8287,"Regular","SPS-3","Present"],
#                          [5089,"Casual","SPS-3","Not Present"],
#                          [3002,"Contract","SPS-4","Present"],
#                          [28089,"Contract","SPS-4","Not Present"],
#                          [1235,"Contract","SPS-5","Present"],
#                          [9897,"Contract","SPS-5","Not Present"]],columns=["P#","Appt_stat","Scale","Avail"])
# pivot = emp_data.pivot_table(index=["Appt_stat","Avail"],columns="Scale",aggfunc="size",fill_value=0)
# print(emp_data)
# bool_series = (df["Appt_stat"] == "Contract") | (df["Scale"] == "SPS-5")
# filtered_rows = df[bool_series]
# print(filtered_rows)
