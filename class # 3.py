# =========
import python_functions as p

p.add(10,15)

import math
import random
import turtle

# res = math.pow(4,2)
# print(16**(1/2))
# res = math.sqrt(16)
# print(res)
# res = math.ceil(1.6)
# print(res)
# res = math.floor(1.6)
# print(res)
# res = math.ceil(2.1)
# print(res)
#
# res = math.ceil((random.random()) * 100)
# print(res)
#
# res = random.randrange(1,100)
# print(res)

res = random.choice(["Ahmed","Kazim","Abdullah"])
print(res)
num_list = [1,2,3,4,5,6]
random.shuffle(num_list)
print(num_list)
















# TASKS of NESTED FOR LOOP
# Task # 1 : Write a program that prints a square pattern using nested for loops.
# The program should prompt the user for the side length of the square.
# Task # 2 :Write a program that prints the multiplication table of numbers from 1 to 10 using nested for loops.
# Task # 3 :Write a program that prints a Triangle pattern using nested for loops.
# Task # 4 :Write a program that prints a Pyramid pattern using nested for loops.
# Task # 5 :Write a program that prints a diamond pattern using nested for loops.
#
# length = 5
# for i in range(0):
#     print("Hello", i)
# print("After for loop")


# for i in range(1,length+1): #(1,6)
#     for j in range(l): #(1,4)
#         print("*", end=" ")
#     for k in range(i): #(0,4) 0-3
#         print("*", end=" ")
#     for l in range(i-1):
#         print(" ", end=" ")
#     print()
#
# for i in range(1,length+1): #(1,6)
#     for j in range(length-i): #(1,4)
#         print(" ", end=" ")
#     for k in range(i): #(0,4) 0-3
#         print("*", end=" ")
#     for l in range(i-1):
#         print("*", end=" ")
#     print()

#         *
#       * * *
#     * * * * *
#   * * * * * * *
# * * * * *  * * * *


# for i in range(1,length+1): #(1,6)
#     for j in range(i): #(1,4)
#         print("*", end="")
#     for k in range(length-i): #(0,4) 0-3
#         print("@", end="")
#
#     print()

# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if (i == 1 and j == 3) or (i == rows and j == 3) or (i == 3 and j == 1) or (i == 3 and j == rows):
#             print(i*j, end=" ")
#         elif (i == 3 and j == 3):
#             print(i+j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i == 1 or i == rows:
#             if j == 3:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#         elif i == 3:
#             if j == 1 or j == 5:
#                 print("*", end=" ")
#             else:
#                 print(" ", end=" ")
#     print()

# rows=5
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i==1 or i==5:
#             if j==3:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         if i==3:
#             if j==1 or j==5:
#                 print("*",end=" ")
#             else:
#                 print(" ",end=" ")
#         else:
#             if j<rows+1:
#                 print(" ",end=" ")
#     print()


# def rec(x):
#     if x == 10000:
#         return 0
#     result = x + rec(x+1)
#     return result
#
# print(rec(1))

# def pattern(n):
#     if n == 0:
#         return ""
#     return " " * (n - 1) + "*" + pattern(n - 1)
#
#
# print(pattern(5))


# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i == 1 or i == rows or j == 1 or j == 5:
#             print(j, end=" ")
#         else:
#             print(" ", end=" ")
#     print()

# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i == 1 or i == rows:
#             if j == 1 or j == rows:
#                 print(i, end=" ")
#             elif j == 3:
#                 print(j, end=" ")
#             else:
#                 print(" ", end=" ")
#         elif i == 3:
#             if j == 1 or j == rows:
#                 print(i, end=" ")
#             elif j == 3:
#                 print(j, end=" ")
#             else:
#                 print(" ", end=" ")
#
#     print()


# rows = 5
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if i == 1 or i == rows:
#             if j == 1 or j == rows:
#                 print(i, end="")
#             else:
#                 print(" ", end="")
#         elif i == 3:
#             print(j, end="")
#         else:
#             if j < 4:
#                 print(i+j, end="")
#     print()

# for i in range(1,length):
#     for j in range(1,length-2): #(1,4)
#         print("*", end="")
#     for k in range(1,length-4): #(1,2)
#         print("@", end="")
#     for l in range(1,length-4): #(1,2)
#         print("&",end="")
#     print()
# rows = 6
# start  = 1
# for i in range(start,rows):
#     for j in range(start,rows):
#         if i == 1 or i == rows-1:
#             if j < 3:
#                 print("*",end=" ")
#             else:
#                 continue
#         else:
#             print("x", end=" ")
#     print()
# * * x x x x x
# x x x x x
# x x x x x
# x x x x x
# * *

# for i in range(rows):
#     for j in range(rows):
#         if i%2 == 0:
#             if j < 3:
#                 print("*",end=" ")
#         else:
#             if j < 1:
#                 print("*", end=" ")
#     print()
# for i in range(1,rows+1):
#     for j in range(1,rows+1):
#         if j <= rows - i or j> (rows - i)+1:
#             print(" ",end="")
#         else:
#             print("*", end="")
#     for k in range(1,i):
#         if k == (i-1):
#             print("*",end="")
#         else:
#             print(" ", end="")
#     print()
# for z in range(1,rows):
#     for l in range(1,rows+1):
#         if l <= i:
#             print(" ",end="")
#         else:
#             print("*", end="")

# for i in range(10,12,2):
# for i in range(10,rows + 10):
#     for j in range(10,(10-2*(i-9)),-2):
#         print(j, end=" ")
#     print()
# start = 10
# for i in range(start,rows+start):
#     for j in range(start,i+1):
#         print(j,end="")
#     print()
# for i in range(1,rows+1): # (1,6) 1-5
#     for j in range(1,(rows + 1 + 1)-i):
#         print("*", end="")
#     print()
    # for j in range(i, (rows + 1 + 1) - i):  # (1,6)



matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
# print(x)
# try:
#     print(x)
# except:
#     print("An error has occured")
# else:
#     print("Error not occured")
# finally:
#     print("Ill run in each case")



# print("Code is continue....")




# for i in matrix1: # [1, 2, 3]
#     for x in range(len(matrix1)):
#         for j in i: # 1,2,3
        # 1*9 , 2*6, 3*3
        # 1*8 , 2*5, 3*2
        # 1*7 , 2*4, 3*1

        # j*matrix2[0][] , j*6, j*3
        # j*8 , j*5, j*2
        # j*7 , j*4, j*1



# outer_counter = 0
# new_matrix = []
# for i in matrix1:
#     outer_counter = outer_counter + 1
#     inner_counter = 0
#     row_add = 0
#     for j in i:
#         inner_counter = inner_counter + 1
#         row_add += j*matrix2[inner_counter-1][outer_counter-1]
#     new_matrix.append(row_add)
#
# print(new_matrix)





# sets = ["a","b","c","d"]
# for i in range(len(sets)):
#     for j in range(i+1,len(sets)):
#         for k in range(j+1,len(sets)):
#             print(sets[i]+sets[j]+sets[k])
# students = ["Std1","Std2","Std3","Std4"]
# cities=["karachi","lahore","quetta","peshawar","rawalpindi"]
# new_cities=cities.pop(0)
# cities.append(new_cities)
# print(cities)
# new_cities=cities[::-1]
# print(new_cities)


# sum=0
# for i in numbers:
#     sum=sum+i
# print(sum)
# print(students[len(students)-2])

# subjects=["english","maths","chemistry"]
# students=["hasann","basit","shahria","ali"]
# for i in subjects:
#     for j in i:
#         # number=int(input("enter number"))
#         print(j)



# TASKS FOR lIST
# Task # 1 :Given two lists of integers, write a program to find and print the common elements between the two lists.
# list=[4,5,6,7]
# list_2=[3,4,1,7]
# new_list=[]
# for i in list:
#     for j in list_2:
#         if i==j:
#             new_list.append(j)
# string=
# for i in 5:
#     print(i)



# Task # 2 :Write a list of numbers as input and  the maximum and minimum values in the list.
# list=[45,67,12,109,67]
# sorted_list=sorted(list)
# print(sorted_list[0])
# print(sorted_list[len(sorted_list)-1])

# Task # 3 :Write a program that reverses a list of integers without using any built-in functions or methods.
# Task # 4 :Given a list of numbers, write a program to remove all the even numbers from the list and print the updated list.
# Task # 5 :Given a list of strings, create a new list containing only the strings that have more than 5 characters.

# def merge_sort(list1):
#     print("Entering List: ",list1)
#     if len(list1) <= 1:
#         print("Returned List due to 1 length: ", list1)
#         return list1
#
#     mid = len(list1) // 2
#     left = merge_sort(list1[:mid])
#     print("Left List after recurssion: ", left)
#     right = merge_sort(list1[mid:])
#     print("Right List after recurssion: ", right)
#
#     return merge(left, right)
#
# def merge(left, right):
#     print("This is left Right: ",left,right)
#     result = []
#     while left and right:
#         if left[0] < right[0]:
#             result.append(left.pop(0))
#         else:
#             result.append(right.pop(0))
#     # print(left)
#     # print(right)
#
#     result.extend(left)
#     result.extend(right)
#     print("Result Appended", result)
#     return result
#
# list1 = [10, 5, 2, 2, 2, 1, 8, 9, 6]
# print("Unsorted list:", list1)

# sorted_list = merge_sort(list1)
# print("Sorted list:", sorted_list)
# row = 6
# col = 10
# for i in range(1,row):
#     for j in range(i):
#         # print(f'Value of outer loop {i} and Value of inner loop {j}')
#         print("*",end="")
#     for k in range(col-i-i):
#         print(" ",end="")
#     for l in range(i):
#         print("*", end="")
#     print()
# *
# **
# ***
# ****
# *****
# *****

# str =  "My name is basit Ali Khan"
# list_str = str.split()
# print(list_str)
# abc = "asmgjktiuehnfkghsurkgnskfhgoiemfn"
# dict_count = {}
# for i in abc:
#     if i not in dict_count:
#         dict_count[i] = 1
#     else:
#         letter_frequency = dict_count[i]
#         letter_frequency = letter_frequency + 1
#         dict_count[i] = letter_frequency
# print(dict_count)


# counter = 0
# for i in list_str:
#     counter = counter + 1
#     if counter > 3:
#         break
#     else:
#         inner_counter = 0
#         for j in i:
#             inner_counter = inner_counter + 1
#             if inner_counter == 4:
#                 print(j)
#             else:
#                 continue


