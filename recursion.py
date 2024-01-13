# +++++++++++  ========================


def find_index(original_str, substring):

  for i in range(len(original_str)):
    if original_str[i:i + len(substring)] == substring:
      return i
  return -1



original_str = "GeeksforGeeks"
substring = "for"

index = find_index(original_str, substring)
print(index)




# Example usage:
# original_str = "GeeksforGeeks"
# substring = "Fr"
# count = 0
# for i in range(len(original_str) - len(substring) + 1):
#     found = True
#     for j in range(len(substring)):
#         if original_str[i + j] != substring[j]:
#             found = False
#             break
#     if found:
#         count += 1
# print(count)
#
# def count_substring_occurrences(original_str, substring):
#     count = 0
#     for i in range(len(original_str) - len(substring) + 1):
#         found = True
#         for j in range(len(substring)):
#             if original_str[i + j] != substring[j]:
#                 found = False
#                 break
#         if found:
#             count += 1
#     return count
#
# # Example usage:
# original_str = "GeeksforGeeks"
# substring = "Gee"
#
# occurrences = count_substring_occurrences(original_str, substring)
# print(f'The substring "{substring}" occurs {occurrences} times in the original string.')

import numpy as np
# import pandas as pd
# employees_data = [[8639,"Basit","CO","SPS-4","Karachi"],
#                   [3002,"Shahriar","GM","SPS-10","Islamabad"],
#                   [10095,"Salman","PCO","SPS-6","Lahore"],
#                   [6023,"Yasir","JTO","SPS-5","Karachi"],
#                   [7970,"Arif","Tech-IV","SPS-1","Lahore"],
#                   [6564,"Ahmed","CO","SPS-4","Karachi"],
#                   [5434,"Usman","GM","SPS-10","Islamabad"],
#                   [4325,"Huma","PCO","SPS-6","Lahore"],
#                   [6432,"Imran","JTO","SPS-5","Karachi"],
#                   [6435,"Azlaan","Tech-IV","SPS-1","Islamabad"],
#                   ]
# df = pd.DataFrame(employees_data,columns=["Country_Name","Name","Desig","Scale","City"])
# count_city = df["Desig"].value_counts()
# print(count_city)
# new_filter = df[df["country_Name"] == "Argentine"]
# print(new_filter)
# print((df["City"] =="Karachi").info())

# arr = [[22,44,np.nan],[33,65,34],[np.nan,12,42]]
# df = pd.DataFrame(arr,columns=["A","B","C"])
# print(info_df)
# info_df = df.info()
# data_after_deletion = df.drop(1,inplace=True)
# print(df)
# print(data_after_deletion)
# data_after_deletion = df.drop("A",axis=1,inplace=True)
# print(df)
# print(data_after_deletion)
# df.dropna(inplace=True)
# df.dropna(axis=1,inplace=True)
# df.fillna("Missing",inplace=True)
# print(df)
















# arr = [[1,4,7],[2,7,9],[8,6,5]]
# df = pd.DataFrame(arr,columns=["A","B","C"])
#
# df["D"] = [6,8,7]
# # print(len(df))
# df.loc[len(df)] =  {"A":2,"B":4,"C":6,"D":8}
# # print(df["B"].loc[1])
#
# # df.loc[0] = df.loc[1] * df.loc[2]
# # df["E"] = 50
# df["Sum"] = np.sum(df,axis=1)
# print(df)
# df["Mean"] = np.mean(df.iloc[:,:-1],axis=1)
# # print(df)
# print(df)
# df["std"] = np.std(df.iloc[:,:-2],axis=1)
# print(df)












# excel_file =pd.ExcelFile("testing_data.xlsx")
# sheets = excel_file.sheet_names
# print(sheets)
# lst = [1,4,6,8,9,12]
# kth_value = 12
# start = 0
# end = len(lst)-1
# midpoint = 0
# while midpoint != kth_value:
#     if ((start + end) + 1)%2 == 0:
#         first_mid_position = int((start + end)/2)
#         second_mid_position = int(((start + end)/2)+1)
#         first_midpoint = lst[first_mid_position]
#         second_midpoint = lst[second_mid_position]
#         median = (first_midpoint + second_midpoint)/2
#         if median > kth_value:
#             end = first_mid_position
#         elif median < kth_value:
#             start = second_mid_position
#     else:
#         mid_position = int((start + end)/2)
#         midpoint = lst[mid_position]
#         if midpoint == kth_value:
#             print("Success! ",mid_position)
#         elif midpoint >kth_value:
#             end = mid_position-1
#         elif midpoint < kth_value:
#             start = mid_position + 1

















import numpy as np
import pandas as pd
# df = pd.read_csv("wages.csv")
# my_dict = {
#     "P#":[8639,5089,np.nan,9999],
#     "Name":["Basit","M Ali","Shahriar","Nadeem"],
#     "Desig":["CO","Mgr","GM",np.nan]
# }
# df2 = pd.DataFrame(my_dict)
# print(df.info())
# df["percentage"] = [50] * len(df)
# df2.dropna(axis=1,inplace=True)
# new_filter = df2[(df2["P#"] == 8639) | (df2["Desig"] == "Mgr")]
# print(df2)
# df2.iloc[:1,0] = 5555
# print(df2)
# df2["Scale"] = ["SPS3","SPS9","SPS10","SPS11"]
# new_df2 = df2.assign(Scale = ["SPS3","SPS9","SPS10","SPS11"])
# df2.insert(1,"Scale",["SPS3","SPS9","SPS10","SPS11"])
# new_after_drop = df2.drop("P#",axis=1,inplace=True)
#
# print(df2)
# print(new_after_drop)






















# my_dict = {
#     "P#":[8639,5089,3002,9999],
#     "Name":["Basit","M Ali","Shahriar","Nadeem"],
#     "Desig":["CO","Mgr","GM","DCM"]
# }
# df = pd.DataFrame(my_dict)
# new_col = ["SPS-4","SPS-9","SPS-10","SPS-11"]
# df["Scale"] = new_col
# agr_col = [29,40,60,59]
# df["age"] = agr_col
# new_row = {
#     "P#": 5265,
#     "Name": "Ali",
#     "Desig": "AM",
#     "Scale":"SPS-10",
#     "age":50
# }

# Use the 'loc' method to add the new row
# df = df.append(new_row,ignore_index=True)
# # print(df)
# new_df = df.drop("P#",axis=1,inplace=True)
# print(new_df)
# df = df.assign(age = agr_col)
# df.insert(2,"age",agr_col,True)
# print(df["age"].describe())
# print(df[df["P#"] == 3002])
# df["Random"] = ["XYZ"] * len(df)
# print(df)
# arr = [[1,1,1],[2,1,2],[3,2,3]]
# df = pd.DataFrame(arr,index=["row1","row2","row3"], columns=["col1","col2","col3"])
# print(df)
# access_col1 = df["P#"]
# access_col2 = df["Name"]
# access_col3 = df["Desig"]

# access_col1andcol2 = df[["P#","Name","Desig"]]
# access_row1 = df["Name"].loc[0]
# print(access_row1)






























# arr = [[3,6,5],[8,6,5],[2,5,7]]
# pandas_df = pd.DataFrame(arr,index=["row1","row2","row3"],columns=["col1","col2","col3"])
# new_colum = [11,22,33]
# pandas_df["col4"] = new_colum
# pandas_df["col5"] = [True] * len(pandas_df)
# pandas_df["col5"] = [np.NaN] * len(pandas_df)
# pandas_df.insert(1,"colabc",[1,1,1],True)
# pandas_df.assign(ABC)
# print(pandas_df[["col1","col2"]].loc[["row1","row2"]])
# print(pandas_df.iloc[:,2])
# df = pd.read_csv('data.csv')
# print(pandas_df)
# random_arr = np.random.randint(1,1000,[50,4])
# df = pd.DataFrame(random_arr,columns=["Day1","Day2","Day3","Day4"])
# header = df.head(10)
# print(header)
# tail = df.tail(2)
# print(tail)
# information = df.info()
# print(information)
# desc = df["Day1"].describe()
# print(df)
# print(desc)






















# print(df.describe())

# Replace 'your_file.csv' with the actual CSV file path
# file_path = 'data.csv'

# Read the CSV file into a Pandas DataFrame
# df = pd.read_csv(file_path)
# Assuming that all data is in the first column, which is separated by semicolons
# Split the data in the first column by semicolon into multiple columns
# df[['Column1', 'Column2', 'Column3']] = df['YourColumnName'].str.split(';', expand=True)

# Now, you have separate columns for the data
# print(df)


# arr = np.array([[100,105],
#                 [105,103],
#                 [103,110],
#                 [102,119]])
# print(arr.shape)
# X = arr[:,0] # [100,105,103,102]
# [
#  [100],
#  [105],
#  [103],
#  [102]
#  ]
# Y = arr[:,1]
# reshape_x = X.reshape(-1,1) #(n_samples,n_features) (4,1)
# reshape_y = Y.reshape(-1,1) #(n_samples,n_features)
# print(reshape_x)
# print(reshape_y)
# new_arr = arr.reshape(4,3)
# print(new_arr)
# copy_of_arr = arr.copy()
# np.random.shuffle(copy_of_arr)
# print(arr)
# print(copy_of_arr)

# view_of_arr = arr.view()
# np.random.shuffle(view_of_arr)
# print(arr)
# print(view_of_arr)






# random_matrix = np.random.randint(1,1000,size=(3,3))
# random_matrix2 = np.random.randint(1,500,size=(3,3))
# dot_product = np.dot(random_matrix,random_matrix2)
# # print(dot_product)
# transpose_matrix = np.transpose(dot_product)
# inverse_matrix = np.linalg.inv(transpose_matrix)
# print(inverse_matrix)
# det_matrix = np.linalg.det(inverse_matrix)
#
# print(det_matrix)



# marks = np.array([43,76,54,56,88,76,23,65,89,76])
# np.random.shuffle(marks)
# new_array = np.random.permutation(marks)
# print(marks)
# print(new_array)

# random_matrix = np.random.rand(3,4)
# print(random_matrix)
# random_normal_matrix = np.random.randn(3,3)
# print(random_normal_matrix)
# print(np.mean(random_normal_matrix))
# print(np.std(random_normal_matrix))
# random_matrix_int = np.random.randint(1,100,size=(3,3))
# print(random_matrix_int)
























# marks = np.array([22,33,44,55,66,77])
# mean_value = np.mean(marks)
# std_value = np.std(marks)
# standardized_marks = (marks-mean_value)/std_value
# print(standardized_marks)
# matrix = np.array([
#     [22,5435],
#     [4,76546],
# ])










# X = np.random.randint(100, 5)  # Feature matrix with 100 samples and 2 features
# y = np.random.randint(0, 2, 100)
# print(X,y)
# np.random.shuffle(marks)
# print(marks)
# print(np.random.permutation(marks))















# Generate random data with some noise
# np.random.seed(0)
# X = 2 * np.random.rand(100, 1)
# y = 4 + 3 * X + np.random.randn(100, 1)
# print(y)
# # Split the data into training and testing sets
# split_ratio = 0.8
# split_index = int(split_ratio * len(X))
# X_train, X_test = X[:split_index], X[split_index:]
# y_train, y_test = y[:split_index], y[split_index:]
# print(X_train)
# print(X_test)
# print(y_train)
# print(y_test)










# Create a dataset of exam scores
# exam_scores = np.array([90, 75, 85, 60, 95, 70])

# Compute the mean and standard deviation
# mean_score = np.mean(exam_scores)
# std_deviation = np.std(exam_scores)
#
# min_val = np.min(exam_scores)
# max_val = np.max(exam_scores)
# normalized_scores = (exam_scores-min_val)/ (max_val-min_val)

# Z-score standardization formula
# standardized_scores = (exam_scores - mean_score) / std_deviation
#
# # Print the original and standardized scores
# print("Original Scores:", exam_scores)
# print("Standardized Scores (Z-scores):", standardized_scores)
# print("Normalized Scores ():", normalized_scores)





# scores = np.array([90,75,85,60,95,70]) # Scale [0-100]
# min_score = np.min(scores)
# max_score = np.max(scores)
# print(min_score)
# print(max_score)
# normalized_scores = (scores - min_score) / (max_score-min_score)
# print("Original Score: ",scores)
# print("Normalised Score: ",normalized_scores)
# houses = np.array([
#     [1500,3,400000],
#     [1000,6,250000],
#     [2000,2,60000000],
#     [1200,8,30000000]
#
# ])
#
# min_val = np.min(houses,axis=0)
# max_val = np.max(houses,axis=0)
# normalized_data = (houses-min_val)/ (max_val-min_val)
# print(normalized_data)
















# vector_mean = np.mean(numpy_vector)
# vector_median = np.median(numpy_vector)
# vector_std = np.std(numpy_vector)
#
# print(vector_mean)
# print(vector_median)
# print(vector_std)
# numpy_arr = np.array(matrix)
# matrix_mean = np.mean(numpy_arr,axis=0)
# matrix_median = np.median(numpy_arr,axis=0)
# matrix_std = np.std(numpy_arr,axis=0)
# print(matrix_mean)
# print(matrix_median)
# print(matrix_std)
# sum = np.sum(numpy_arr,axis=1)
# print(sum)

# print(numpy_arr[0,0:2])
# print(numpy_arr[:,-1])












# means_axis0 = np.mean(numpy_arr,axis=0)
# means_axis1 = np.mean(numpy_arr,axis=1)
# print(means_axis0)
# print(means_axis1)
# 3x + y = 9
# x + 2y = 8
# coefficients = np.array([[3,1],
#                          [1,2]])
# rhs = np.array([9,8])
#
# solution = np.linalg.solve(coefficients,rhs)
# print(solution)
# print("Value of X is: ",solution[0])
# print("Value of Y is: ",solution[1])

# D = np.linalg.det(coefficients)

# coeff_x = coefficients.copy()
# coeff_y = coefficients.copy()

# coeff_x[:,0] = rhs
# coeff_x = [[9,1],
#            [8,2]]
# coeff_y[:,1] = rhs
# coeff_y = [[3,9],
#            [1,8]]
# Dx = np.linalg.det(coeff_x)
# Dy = np.linalg.det(coeff_y)
#
# x = Dx / D
# y = Dy / D
#
# print(x)
# print(y)






# matrix = [[1,4,7],
#           [3,9,8],
#           [0,0,0]]
# matrix_of_ones = np.ones([3,3],dtype=int)
# identity_matrix = np.eye(3,dtype=int)
# oneslike = np.ones_like(matrix)

# print(matrix_of_ones)
# print(identity_matrix)
# addition = matrix_of_ones + identity_matrix
# det_matrix_addition = np.linalg.det(addition)
# det_matrix = np.linalg.det(matrix)
# print(addition)
# print(det_matrix_addition)
# print(det_matrix)
# print(matrix)
# transpose = np.transpose(matrix)
# print(addition)
# dot_product = np.dot(matrix,addition)
# transpose = np.transpose(dot_product)
# print(transpose)



# list_1 = [[2,4,5],[3,5,6],[7,8,9]]
# arr_list = np.array(
# [
#     [2,4,5,4],
#     [3,5,7,9],
#     [7,8,1,6]
# ])
# print(list_1[0][1])


# print(type(arr_list))
# print(arr_list.ndim)
# print(arr_list.shape)
# print(np)




# list_1 = [5,3,2,5,3,7]
# new_list = [[],[],[]]
# new_list[0].append(5)
# new_list[0].append(6)
# new_list[0].append(7)
#
# new_list[1].append(8)
# new_list[1].append(9)
# new_list[1].append(10)
#
# new_list[2].append(11)
# new_list[2].append(12)
# new_list[2].append(13)
# print(new_list)
# first_number = 1
# factor = 5
# first_number  =  5
# second_number = 3
# while len(list_1) > 1:
#     first_number = first_number * 2
#     second_number = second_number * 2
    # factor = list_1[0]
    # result = factor + 1
    # new_list.append(result)
    # del list_1[0]
    # del list_1[2]


# 10 * 9 * 8 * 7 * 6 * 0
# 10 * abc(10-1)
# 9 * abc(9-1)
# 8 * abc(8-1)
# 7 * abc(7-1)
# 6 * abc(6-1)
# return 1
# def abc(x):
#     if x == 0:
#         return 1
#     else:
#         abc(x - 1)
#         print(x)
#
# print(abc(5))







# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
#
# nterms = 10
#
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))





import timeit

import timeit

#
# def main():
#     number_from_user = 1000
#     flag = False
#     if number_from_user == 0 or number_from_user == 1:
#         print("the number is not a prime number")
#     elif number_from_user > 1:
#         for i in range(2, number_from_user):
#             if number_from_user % i == 0:
#                 flag = True
#                 break
#     if flag == True:
#         print("its a composite number")
#     else:
#         print("its a prime number")




# print(timeit.timeit("main()", number=10))
# def main():
#     n = 5
#     if n == 0:
#         return 1
#     return n * main(n - 1)
#
#
# print(timeit.timeit("main()", number=1))
# str = "2+8-3*5"
# str = list(str)
# while len(str) > 1:
#     target_op = str.find("/")
#     print(target_op)
    # if str[1] == "+":
    #     str[0] = int(str[0])+int(str[2])
    #     del str[1]
    #     del str[2]
    # elif str[1] == "-":
    #     str[0] = int(str[0])-int(str[2])
    #     del str[1]
    #     del str[2]
    # elif str[1] == "*":
    #     str[0] = int(str[0])*str[2]
    #     del str[1]
    #     del str[2]
# print(str)

