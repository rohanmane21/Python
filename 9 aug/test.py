# t=(10,20,30)
# print(t)
# set={8,5,3,1}
# print(set)
# def add(a,b):
#     c=a+b
#     print(c)#print(" I am Rohan From Pune. \n I have completed Btech In Information Technology from RSCOE.\n I am 21 years old ")
# add(5,5)
# def a():
#     s=str(input("Enter Your Name:"))
#     print("Hello",s)
# a()

# def fun(a,b,c):
#     print("Greatest Number",max(a,b,c))
# fun(2,3,6)
# def greatest():
#     a=int(input("Enter A:"))
#     b=int(input("Enter B:"))
#     c=int(input("Enter C:"))
#     if type(a)==type(int) and type(b)==type(int) and type(c)==type(int):
    
#         if a>b and a>c:
#             print("Gretest Number is A=",a)
#         elif b>c and b>a:
#             print("Gretest Number is B=",b)
#         elif c>b and c>a:
#             print("Gretest Number is C=",c)
#     else:
#         print("Invalid Input")
# greatest()
# def add(a):
#     print(a)
#     return add(4)
# add(2)


# *Question 1:*
# Write a Python function named `calculate_average` that takes a list of numbers as a parameter and returns the average of those numbers.
# def calculate_average():
#     lst=[]
#     n=int(input("Enter number of elements : "))
#     for i in range(0,n):
#         ele=int(input())
#         lst.append(ele)
#     sum =0
#     avg=0
#     for i in lst:
#         sum+=i
#         avg=sum/n
#     print(avg)
# calculate_average()


# *Question 2:*
# Create a function `find_max_min` that takes a list of numbers as input and returns a tuple containing the maximum and minimum values in the list.
# def find_max_min():
#     lst=[]
#     n=int(input("Enter number of elements : "))
#     for i in range(0,n):
#         ele=int(input())
#         lst.append(ele)
#     maximum=max(lst)
#     minimum=min(lst)
#     print("MAX MIN :",(maximum,minimum))
# find_max_min()

# *Question 3:*
# Write a function `is_prime` that takes an integer as an argument and returns `True` if it's a prime number, and `False` otherwise.
# def is_Prime(n):
#     if (n==1):
#         return False
#     elif(n==2):
#         return True
#     else:
#         for i in range(2,n):
#             if(n%i==0):
#                 return False
# print(is_Prime(2))

# *Question 4:*
# Create a function `reverse_string` that takes a string as input and returns the string in reverse order.
# def reverse_string():
#     st=""
#     s=str(input("Enter String: "))
#     for i in s:
#         st=i+st
#     print(st)
# reverse_string()

# *Question 5:*
# Write a function `count_vowels` that takes a string as input and returns the count of vowels (both lowercase and uppercase) in the string.
# def count_vowels():
#     s="rohanmane"
#     count=0
#     for i in s:
#         if (i=='a'or i=='e'or i=='i' or i=='o' or i== 'u'or i=='A'or i=='E'or i=='I' or i=='O' or i== 'O'):
#             count+=1
#     if count== 0:
#         print("No Vowels Found")
#     else:
#         print("Number of Vowels:",count)
# count_vowels()

# *Question 6:*
# Create a function `unique_elements` that takes two lists as parameters and returns a new list containing only the unique elements from both lists.
# def unique_elements(list1, list2):
#     set1 = set(list1)
#     set2 = set(list2)
#     if(set1.intersection(set2)):
#         print("Common elements: " + str(set1.intersection(set2)))
#     else:
#         print ("No common elements")

# list1 = [3, 6, 9, 12, 15]
# list2 = [2, 4, 6, 8, 10, 12, 14]
# unique_elements(list1, list2)


# *Question 7:*
# Write a function `power_list` that takes a list of numbers and a power as arguments and returns a new list with each number raised to the given power.
def power_list():
   test_list = [6, 9, 1, 8, 4, 7]
   print("The original list is : " + str(test_list))
   res = []
   for i,ele in enumerate(test_list):
    res.append(ele ** i) 
   print("Powered elements : " + str(res))
power_list()

# *Question 8:*
# Create a function `remove_duplicates` that takes a list as input and returns a new list with duplicate elements removed while maintaining the original order.
# *Question 9:*
# Write a function `matrix_transpose` that takes a 2D matrix (list of lists) as input and returns the transpose of the matrix.

# def matrix_transpose(l1, l2):
# # iterate list l1 to the length of an item
# 	for i in range(len(l1[0])):
# 		r =[]
# 		for item in l1:
# 			r.append(item[i])
# 		l2.append(row)
# 	return l2
# l1 = [[1, 2, 3, 9], [4, 2, 8, 9], [7, 6, 4, 1]]
# l2 = []
# print(matrix_transpose(l1, l2))

# *Question 10:*
# Create a function `find_common_elements` that takes two lists as parameters and returns a new list containing the common elements between the two lists.
# def find_common_elements(list1, list2):
#     c = []
    
#     for item in list1:
#         if item in list2:
#             c.append(item)   
#     return c
# list1 = [1, 2, 3, 4, 5]
# list2 = [3, 4, 5, 6, 7]
# c = find_common_elements(list1, list2)
# print(c)  

# *Question 11:*
# Write a function `fibonacci_sequence` that generates the first n numbers in the Fibonacci sequence as a list. The function should take `n` as an argument.
# def Fibonacci(n):
# 	if n < 0:
# 		print("Incorrect input")
# 	elif n == 0:
# 		return 0
# 	elif n == 1 or n == 2:
# 		return 1
# 	else:
# 		return Fibonacci(n-1) + Fibonacci(n-2)
# print(Fibonacci(8))

# *Question 12:*
# Create a function `capitalize_titles` that takes a list of strings (book titles) as input and returns a new list with the titles properly capitalized (capitalize the first letter of each word except for common words like "and", "the", "of", etc.).

# *Question 13:*
# Write a function `flatten_list` that takes a nested list as input and returns a flat list containing all the elements.

# *Question 14:*
# Create a function `largest_continuous_sum` that takes a list of integers and finds the largest sum of continuous elements in the list.

# *Question 15:*
# Write a function `anagram_check` that takes two strings as input and returns `True` if the strings are anagrams (contain the same characters in different orders), and `False` otherwise.

# *Question 16:*
# Create a function `binary_search` that performs a binary search on a sorted list and returns the index of the target element if found, or `-1` if not found.

# *Question 17:*
# Write a function `flatten_dictionary` that takes a nested dictionary as input and returns a flattened dictionary where the keys are concatenated with parent keys using underscores.

# *Question 18:*
# Create a function `prime_factors` that takes an integer as input and returns a list of its prime factors.

# *Question 19:*
# Write a function `shuffle_list` that takes a list as input and returns a new list with the elements shuffled randomly.

# *Question 20:*
# Create a function `run_length_encoding` that takes a string as input and returns its run-length encoded version. For example, `"aaabbbccaa"` should become `"3a3b2c2a"`.

# Feel free to adapt the complexity and requirements of these practical questions according to your needs.