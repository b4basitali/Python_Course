
# 1
# a
# print
# +++++++++++  ========================

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
print(str)

