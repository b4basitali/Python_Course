# Task # 1: Write a function that takes two numbers as input and print their sum.

# def sum():
#     a=int(input("write down number"))
#     b=int(input("write down number"))
#     c=a+b
#     print(c)
#
# sum()
# Task # 2: Write a function that reverses a given string.
# def string():
#     string=input("enter string")
#     a=string[::-1]
#     print(a)
#
# string()

# The function should take a string as input and return the reversed string.


# Task # 3: Write a function that checks if a given string is a palindrome or not.
# The function should take a string as input and return True if it's a palindrome, and False otherwise.
# def palindrome():
#     string=input("enter string")
#     a=string[::-1]
#     if string==a:
#         print("its a palindrome")
#     else:
#         print("its not a palindrome")
#
# palindrome()

# Task # 4: Write a function that finds the area of a circle given its radius.
# The function should take the radius as input and return the area of the circle.
# def area():
#     radius=int(input("enter radius"))
#     area=((22/7)*radius**2)
#     print(area)
#
# area()
# Task # 5: Write a function that takes a list of integers as input and returns the average of the numbers.
# def average():
#     list=[]
#     sum=0
#     for i in range(5):
#         integer=int(input("enter number"))
#         list.append(integer)
#     for i in list:
#         sum=sum+i
#         average=sum/len(list)
#     print(average)
#
# average()



# Function Definition
# def hello():
#     print("Im your first user defined function")


#Function Call
# hello()
# hello()
# hello()


# Function Definition with parameters
# def hello(a,b):
#     print(f'Im a user defined function and can do anything with upcoming two parameters a = {a} and b = {b}')
#
#
# # Function Call with arguments
# a=5
# b=7
# hello(a,b)

# def calculator(num_1,num_2,op):
#     if op=="+":
#         sum=num_1+num_2
#         return sum
#     elif op=="/":
#         divide=num_1/num_2
#         return divide
#     elif op=="*":
#         multiply=num_1*num_2
#         return multiply
#     else:
#         subtract=num_1-num_2
#         return subtract
#
# num_1=int(input("enter number 1"))
# num_2=int(input("enter number 2"))
# op=input("enter operator")
#
# final=calculator(num_1,num_2,op)
# print(final)

# def subtraction(received_list):
#     largest_number=received_list[len(received_list)-1]
#     smallest_number=received_list[0]
#     subtract=largest_number-smallest_number
#     return subtract
# list=[]
# for i in range(5):
#     number=int(input("enter number"))
#     list.append(number)
# list.sort()
# alpha=subtraction(list)
# print(alpha)

# num_list = [33,45,77,66,44,9,6,33,23,65]
# sorted_list = sorted(num_list)
# print("Actual Num_List after using sorted() function ", num_list)
# num_list.sort()
# print(f"Actual Num_List after using sort() function ", num_list)
main_list=[["hasan","basit"],["ali","shahrian"],["supar","isro"]]
for i in main_list:
    print(i)





