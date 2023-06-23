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





# sum=0
# for i in range(1,5):
#     sum=sum+i
#     print(sum)

l1 = [22,32,33,43,55,65,77,87]
l2 = ["Value1","Value2","Value3","Value4","Value5","Value6"]
new_list = []
for i in range(0,len(l1)):
    if l1[i]%2==0:
        new_list.append(l1[i])
        l1.remove(l1[i])
print(new_list)
print(l1)

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















