# +++++++++++  ========================
import numpy as np
import pandas as pd
df = pd.read_excel('stress.xlsx')
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
# from sklearn.svm import SVC
# model = SVC()
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=1000)
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()


# Assuming df is your DataFrame with the selected features and 'stress_level' as the target variable
X = df[['anxiety_level', 'self_esteem', 'mental_health_history', 'depression', 'headache', 'blood_pressure', 'sleep_quality', 'breathing_problem', 'noise_level', 'living_conditions', 'safety', 'basic_needs', 'academic_performance', 'study_load', 'teacher_student_relationship', 'future_career_concerns', 'social_support', 'peer_pressure', 'extracurricular_activities', 'bullying']]
y = df['stress_level']

print(train_test_split(X, y, test_size=0.2, random_state=42))
#
# # Split the data into training and testing sets
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# # Choose a model (Random Forest in this example)
# model = RandomForestClassifier()

# model.fit(X_train, y_train)
# joblib.dump(model, 'k_neighbor_stress.joblib')
# print(df.iloc[0,:])
# Make predictions on the test set
# y_pred = model.predict(df.iloc[0,:-1].values.reshape(1, -1))
# print(y_pred)


# loaded_model = joblib.load('k_neighbor_stress.joblib')
# #
# y_pred = loaded_model.predict(X_test)
#
# accuracy = accuracy_score(y_test, y_pred)
# print(f"Accuracy: {accuracy}")





# string_one = "geeks4geeks5"
# list_a = []
# counter = 0
#
# while True:
#     value = string_one[counter]
#
#     if value.isnumeric():
#         for i in range(counter + 1, len(string_one)):
#             if string_one[i].isnumeric():
#                 value = value + string_one[i]
#                 counter = counter + 1
#             else:
#                 counter = counter + 1
#                 break
#         else:
#             counter = counter + 1
#
#         list_a.append(value)
#     else:
#         counter = counter + 1
#
#     if counter == len(string_one):
#         break
#     else:
#         continue
#
# print(list_a)

# df1 = pd.DataFrame([[8639,"Basit","SPS-5"],[6598,"Ahmed","SPS-6"],[3257,"Hasan","SPS-7"],[7896,"Kamran","SPS-4"],[5698,"Salman","SPS-10"]],columns=["P#","Name","Scale"])
# df2 = pd.DataFrame([[5423,"MSC",2010],[8639,"BS",2017],[2365,"SSC",2020],[3257,"MBA",2014]],columns=["P#","Degree","Passing_Year"])
# df3 = pd.DataFrame([["Computer Course",2012,8639], ["AI",2018,9898],["Drafting",2020,7896]],columns=["Course_Title","Passing Year","P#"])
#
#
# join_df = pd.merge(df1,df3,on="P#",how="outer")
# print(join_df)























# bins = [1,10,20,30,40,50]
# labels = ["Less then 10","Between 10 and 20", "Between 20 and 30","between 30 and 40","Between 40 and 50"]
# df["anxiety_category"] = pd.cut(df["anxiety_level"],bins=bins,labels=labels)
# print(df)
#






















# s1 = "bcadeh"
# s2 = "hea"
#
# freq_s1 = {}
# freq_s2 = {}
#
# for char in s1:
#     f1 = freq_s1.get(char, 0) + 1
#     freq_s1[char] = f1
# print(freq_s1)
#
#
# for char in s2:
#     freq_s2[char] = freq_s2.get(char, 0) + 1
# print(freq_s2)

# Find the count of characters that are different
# count = 0
# for char in freq_s1:
#     if char in freq_s2:
#         count += abs(freq_s1[char] - freq_s2[char])
#     else:
#         count += freq_s1[char]
# print(count)
#
# for char in freq_s2:
#     if char not in freq_s1:
#         count += freq_s2[char]
#
# print(count)



# lst = "bcadeh"
# lst2 = "hea"
# common_letters = ""
#
# for i in lst:
#     if j in lst2:
#         common_letters += i

# print(common_letters)
# check_pop = lst.pop(2) # delete an element by index number and return the deleted item
# check_remove = lst.remove(9) # delete an element by value and never return the item
# del lst[2]
# print(check_remove)
# while len(lst) > 1:
#     if lst[0] > lst[len(lst)-1]:
#         lst.pop(0)
#     else:
#         lst.pop(-1)
# print(lst)

# print(int(-15/6))
# df = pd.read_excel("stress.xlsx")
# Store the original column names
# original_column_names = df.columns.tolist()

# Convert the DataFrame to a NumPy array
# n = df.to_numpy()
# new_n = (n*100)/(np.max(n,axis=0))
# # print(np.max(n,axis=0))
# df = pd.DataFrame(new_n,columns=original_column_names)
#
# print(df)





# data = np.random.randint(10,20,(4,1))
# df = pd.DataFrame(data, columns=["X"])
# df = pd.DataFrame([["Basit"],["Hasan"],["Ahmed"],["Muhammad Yasir"],["Ali"],["Syed Muhammad Abdullah"]],columns=["Name"])
# print(df)
# x = df["X"]
# new_column = []
# for i in x:
#     new_column.append(i*i)
# df["Sqaure"] = new_column
# print(df)


# def length(x):
#     return len(x)
#
# def square(x):
#     sq = x * x
#     return sq
# def cube(x):
#     return x**3

# df["square of x"] = df["X"].apply(square)
# df["Cube of x"] = df["Value of X"].apply(cube)




#
#
# number_one=14
# number_two=8
# smaller_value=0
# hcf=1
# while True:
#     if number_one<number_two:
#         smaller_value=number_one
#     else:
#         smaller_value=number_two
#
#     for i in range(2,smaller_value+1):
#         count_factors=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count_factors=count_factors+1
#         if count_factors==2:
#             #print(i,"is prime")
#             if number_one%i==0 and number_two%i==0:
#                 number_one=int(number_one/i)
#                 number_two=int(number_two/i)
#                 print(number_one,number_two)





# def even_odd(x):
#     if x%2 == 0:
#         return "Even"
#     else:
#         return "Odd"



#I want have a number i want to check whether it is even or odd
# number = 4534754
# print(even_odd(number))

# n1 = 6,1
# n2 = 24,4
# smaller = 0
# hcf = 0
# while True:
#     if n1> n2:
#         smaller = n2
#     else:smaller = n1
#     for i in range(2,smaller + 1):
#         if (n1%i == 0) and (n2%i == 0):
#             n1 = n1/i
#             n2 = n2/i
#             hcf = i
#             break
#         else
# print(hcf)
# lcm



    # print(i, "is: ", even_odd(i))