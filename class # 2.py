

# nums = [2,7,11,15]
# nums2 = [6,5,154,13]
# for i in enumerate(nums,)
# for j in nums2:
#     print(i,j)
outer_counter = 0
for i in range(3):
    outer_counter = outer_counter + 1
    inner_counter = 0
    for j in range(3):
        inner_counter = inner_counter + 1
        # print(f"Value will go to Box {outer_counter} is we use outer counter")
        print(f"Value will go to Box {inner_counter} is we use inner counter")



# nums = [0,1,2,3,4,5,6,7]
# axis = 3
# nums.extend(nums[:axis])
# del nums[:axis]
# print(nums)
#
# sum =
# list_1 = [[],[],[]]
# list_1[0].append(2)
# list_1[1].append(3)
# list_1[2].append(4)
# print(list_1)
# grand_total = 0
# for i in range(1,10):
#     sub_total = 0
#     for j in range(1,5):
#         add = i+j 1 + 1, 1 + 2, 1 + 3, 1 + 4 = 46
#         grand_total = grand_total + add
#         sub_total = sub_total + add
#         list_1.append(add)
#     print("Sub total: ", sub_total)

#
# print("Grand Total: ",grand_total)
# print("List of sum of each iteration pair: ", list_1)






# nums = [2,7,11,15]
# target = 9
# for i in nums:
#     for j in nums:
#         if int(nums[i]) + 3
# abc
# ab
# abd
# acd
# bcd
# counter = 0
# for i in range(1,11):
#     counter = counter + 1
#     print(counter-1)
    # for j in range(1,11):
        # print(f' {i} x {j} = {i*j}')

# sets = ["a","b","c","d"]
# ab ac ad bc bd cd

# while True:
#     print("Sentiment analysis is inprogress")
#
#     average_polarity = 0.2
#     average_subjectivity = 0.5
#
#     if average_polarity > 0.5:
#         print("Continue the process")
#     else:
#         continue
#
#
#     user_choice = int(input("Do you want to continue? Press 1 to continue: "))
#     if user_choice != 1:
#         break





# TASKS of FOR LOOP
# Task # 1 : calculate the sum of the numbers from 1 to 10 (Using For Loop)
# sum=0
# for i in range(1,11):
#     sum=sum+i
# print(sum)
# Task # 2 : print the multiplication table for the number input by the user (Using For Loop)
# number=int(input("enter number"))
# for i in range(1,11):
#     product=i*number
#     # print(str(i)+"x"+str(number)+"="+ str(product))
#     print(f'{number} x {i} = {product}')



# Task # 3 : calculate the factorial of the number input by the user (Using For Loop)
# number=int(input("enter number"))
# product=number
# for i in reversed(range(1,number)):
#     product=product*i
# print(product)

# str = "abc"
# print(str[1])

# Task # 4 : count the vowels in the string input by the user (Using For Loop)
# string=input('enter string')
# count=0
# vowel="AEIOUaeiou"
# for i in string:
#     if i in vowel:
#         count=count+1
# print(count)


# Task # 5 : Print even numbers from 1 to 10 (Using For Loop)
# for i in range(1,11):
#     if i%2==0:
#         print(i)





# def sentiment_analysis():
#     average_polarity = 0.2
#     average_subjectivity = 0.5
#     return {"polarity":average_polarity,"subjectivity":average_subjectivity}
#
# sentiment = sentiment_analysis()
# if
# sum=0
# for i in range(1,5):
#     sum=sum+i
#     print(sum)

# l1 = [22,32,33,43,55,65,77,87]
# l2 = ["Value1","Value2","Value3","Value4","Value5","Value6"]
# new_list = []
# for i in range(0,len(l1)):
#     if l1[i]%2==0:
#         new_list.append(l1[i])
#         l1.remove(l1[i])
# print(new_list)
# print(l1)

# for i in l1:
#     if i%2==0:
#         new_list.append(i)
#         l1.remove(i)
# print(new_list)
# print(l1)
# del l1[1]
# del l2[1]
#
# l1.remove(43)
# l2.remove("Value2")
#
# l1.pop(3)
# l2.pop(4)
#
# l1.append(99)
# l2.append("Value7")

# print(l1)
# print(l2)















