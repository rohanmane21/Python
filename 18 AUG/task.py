# *Section 1: Basic Concepts*

# 1. Write a Python program that takes two numbers as input and performs basic arithmetic 
# operations (sum, difference, product, quotient).

# class Arithmatic:
#     def __init__(self) -> None:
#         pass

# class sum(Arithmatic):
#     def __init__(self) -> None:
#         super().__init__()
#         self.a=int(input("Enter First Number:"))
#         self.b=int(input("Enter Second Number:"))
#     def sumofN(self):
        
#         print("Sum Of Two Number: ",self.a+self.b)

# class dif(Arithmatic):
#     def __init__(self) -> None:
#         super().__init__()
        
#     def difofN(self):
#         self.a=int(input("Enter First Number:"))
#         self.b=int(input("Enter Second Number:"))
#         print("Difference Of Two Number: ",self.a-self.b)

# class prod(Arithmatic):
#     def __init__(self) -> None:
#         super().__init__()
#         self.a=int(input("Enter First Number:"))
#         self.b=int(input("Enter Second Number:"))
#     def prodofN(self):
#         print(" Product Of Two Number: ",self.a*self.b)

# class qut(Arithmatic):
#     def __init__(self) -> None:
#         super().__init__()
#         self.a=int(input("Enter First Number:"))
#         self.b=int(input("Enter Second Number:"))
#     def qutofN(self):
#         print("Qutient Of Two Number: ",self.a/self.b)


# def main():
#     print("Choose Your Choice \n A. SUM\n B. DIFFRENCE\n C. PRODUCT \n D. QUTIENT")
#     s = input("Enter your choice: ")
#     match s:
#         case 'A':
#             a= sum()
#             a.sumofN()
#         case 'B':
#             b= dif()
#             b.difofN()
#         case 'C':
#             c= prod()
#             c.prodofN()
#         case 'D':
#             d= qut()
#             d.qutofN()
#         case _:
#             print("Invalid Choice")
# main()

# 2. Create a program that generates a list of even numbers within a given range.

# for i in range(0,100):
#     if i%2==0:
#         print(i)
    
# 3. Develop a program that checks if a given number is prime or not.

# def is_Prime(n):
#     if (n==1):
#         print("Not Prime")
#     elif(n==2):
#         print("Prime Number")
#     else:
#         for i in range(2,n):
#             if(n%i==0):
#                 print("Not Prime")
# print(is_Prime(9))

# 4. Write a Python function to calculate the nth term of the Fibonacci sequence.
# Program to display the Fibonacci sequence up to n-th term

# nterms = int(input("How many terms? "))
# # first two terms
# n1, n2 = 0, 1
# count = 0
# # check if the number of terms is valid
# if nterms <= 0:
#    print("Please enter a positive integer")
# # if there is only one term, return n1
# elif nterms == 1:
#    print("Fibonacci sequence upto",nterms,":")
#    print(n1)
# # generate fibonacci sequence
# else:
#    print("Fibonacci sequence:")
#    while count < nterms:
#        print(n1)
#        nth = n1 + n2
#        # update values
#        n1 = n2
#        n2 = nth
#        count += 1

# 5. Implement a program that converts temperature between Celsius and Fahrenheit scales.

# celsius_temp=int(input("Enter Temperature:"))
# fahrenheit_temp =celsius_temp*1.8+32
# print(f"The Fahrenheit equivalent of {celsius_temp}% celsius = { fahrenheit_temp}%")

# 6. Create a function that finds the greatest common divisor (GCD) of two numbers.
# import math
# def gcd():
#     a=int(input("Enter First Number:"))
#     b=int(input("Enter Second Number:"))
#     print("",math.gcd(a,b))
# gcd()

# 7. Write a program to print the multiplication table of a given number.
# n=int(input("Enter Number:"))
# for i in range(1,11):
#     print(i*n)

# 8. Develop a program that generates a random password of a specified length
# import random                       
# def generate_password(len):  
#     list_of_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#₹%^&*()"  
#     pass_str = ""  
#     for i in range(len):  
#         pass_str = pass_str + random.choice(list_of_chars)    
#     return pass_str 
# len = int(input("Enter the length of PASSWORD:"))  
# pass_str = generate_password(len)  
# print("A randomly generated Password is:", pass_str)

# *Section 2: Strings and Lists*

# 9. Write a Python function that counts the occurrences of a specific word in a given sentence.

# str = "Hello Everyone My Name Is Rohan Mane I Am IT Engineer And I Am Working As A DevOps Engineer"
# c = dict()
# txt = str.split(" ")
# for i in txt:
# 	if i in c:
# 		c[i] += 1
# 	else:
# 		c[i] = 1
# print(c)


# 10. Implement a program that removes duplicates from a list while maintaining the original order.
# from collections import OrderedDict
# By using import module
# l = [1, 5, 3, 6, 3, 5, 6, 1]
# print ("The original list is : "+ str(l))
# s = list(OrderedDict.fromkeys(l))
# print ("The list after removing duplicates : "+ str(s))
# initializing list

# test_list = [1, 5, 3, 6, 3, 5, 6, 1]
# print("The original list is : " + str(test_list))
# res = []
# for i in test_list:
# 	if i not in res:
# 		res.append(i)

# # printing list after removal
# print("The list after removing duplicates : " + str(res))


# 11. Create a function that returns the reverse of a string without using string slicing.
# def reverse_string(str):  
#     str1 = ""    
#     for i in str:  
#         str1 = i + str1  
#     return str1 
# str = "JavaTpoint"       
# print("The original string is: ",str)  
# print("The reverse string is",reverse_string(str)) 

# 12. Write a program that finds the longest word in a list of words.

# str = input("Enter a String: ")
# word_list = str.split()
# longest_word = max(word_list, key = len)
# pos = str.index(longest_word)
# print("Longest word: ",longest_word)
# print("Position of Longest word: ", pos)

# 13. Develop a function that sorts a list of strings based on their lengths.
## initializing the list of strings
# def sort():
#     string=" Hello I Am Rohan Mane"
#     s=string.split()
#     print("Before Sorting",s)
#     sorted_list = list(sorted(s, key = len))
#     print("After Sorting",sorted_list)
# sort()

# 14. Implement a program that takes a list of strings and capitalizes the first letter of each word.
# import string
# s = "python is interpreted language"
# print("Original string:",s)
# result = string.capwords(s)
# print("After capitalizing first letter:",result)


# 15. Create a function that determines whether two strings are anagrams.

# def isanagrams():
#     a=input("Enter First Words: ")
#     b=input("Enter First Words: ")
#     if sorted(a) == sorted(b):
#         print("Are Anagrams")
#     else:
#         print("Not Anagrams")
# isanagrams()

# 16. Write a program that removes all vowels from a given string.

# string = "PrepInsta"
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# result = ""
# for char in string:
#     if char not in vowels:
#         result = result + char
# print("\nAfter removing Vowels: ", result)

# *Section 3: Functions*

# 17. Implement a function to calculate the power of a number using recursion.

# def power(a, b):
#     if b != 0:
#         return a * power(a, b - 1)
#     else:
#         return 1
# a = int(input("Enter Number: "))
# b = int(input("Enter Power of Number: "))
# print(a, "to the power", b, "is", power(a, b))

# 18. Write a program that finds the factorial of a given number using a recursive function.

# def factorial(n):

#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)

# num = int(input("Enter a non-negative integer: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     result = factorial(num)
#     print(f"The factorial of {num} is {result}")

# 19. Create a function that calculates the sum of digits in a given number.
# def getSum(n):
#     sum = 0
#     while (n != 0):
#         sum = sum + (n % 10)
#         n = n//10
#     return sum  
# n = 1234
# print(getSum(n))

# 20. Develop a program that generates the prime factors of a given number.
# def Prime_Factorial(n):
#     if n < 4:
#         return n
#     arr = []
#     while n > 1:
#         for i in range(2, int(2+n//2)):
#             if i == (1 + n // 2):
#                 arr.append(n)
#                 n = n // n
#             if n % i == 0:
#                 arr.append(i)
#                 n = n // i
#                 break
#     return arr
# n = 210
# print(Prime_Factorial(n))

# 21. Write a function to compute the LCM (Least Common Multiple) of two numbers.

# def compute_lcm(x, y):
#    # choose the greater number
#    if x > y:
#        greater = x
#    else:
#        greater = y
#    while(True):
#        if((greater % x == 0) and (greater % y == 0)):
#            lcm = greater
#            break
#        greater += 1

#    return lcm
# num1 = 54
# num2 = 24
# print("The L.C.M. is", compute_lcm(num1, num2))

# 22. Implement a program that checks if a given number is a palindrome.

# num = input('Enter any number : ')
# val = int(num)
# if num == str(num)[::-1]:
#     print('The given number is PALINDROME')
# else:
#     print('The given number is NOT a palindrome')

# 23. Create a function that converts a decimal number to binary.

# def dectoBin():
#     n=int(input("Enter Number: "))
#     print(f"{n} in Binary {bin(n)[2:]}")
# dectoBin()

# 24. Write a program that calculates the area of different shapes (circle, rectangle, triangle) 
# based on user input.
# class shape:
#     def __init__(self) -> None:
#         pass

# class circle(shape):
#     def __init__(self) -> None:
#         super().__init__()
#         self.radius = float(input("Enter the Radius:"))

#     def claculat_area(self):
#         print("Area of Circle: ",3.14*self.radius*self.radius)


# class rectangle(shape):
#     def __init__(self) -> None:
#         super().__init__()
#         self.width = float(input("Enter the width:"))
#         self.height = float(input("Enter the height:"))
#     def claculat_area(self):
#         print("Area of Rectangle: ",self.width*self.height) 

# class triangle(shape):
#     def __init__(self) -> None:
#         super().__init__()
#         self.base = float(input("Enter the base:"))
#         self.height = float(input("Enter the height:"))
#     def claculat_area(self):
#         print("Area of Triangle: ",self.base*self.height/2) 

# def main():
#     print("Choose a shape (circle/rectangle/triangle)")
#     s = input("Enter your choice: ")
#     match s:
#         case 'circle':
#             c1 = circle()
#             c1.claculat_area()
#         case 'rectangle':
#             r1 = rectangle()
#             r1.claculat_area()
#         case 'triangle':
#             r1 = triangle()
#             r1.claculat_area()
        
#         case _:
#             print("Invalid Choice")

# main()
# 25. Develop a class `Person` with attributes: name, age, and occupation.

# class person:
#     def __init__(self):
#            self.a=input("Name of Person: ")
#            self.b=int(input("Age of Person: "))
#            self.c=input("Occupation of Person: ")
#            print(f"*********Details of Person*********\nName of Person is {self.a}\nAge of Person is {self.b}\nOccupation of Person is {self.c} ")
# def main():
#       p=person()    
# main()

# 26. Write a program to calculate the total area of multiple rectangles using a class `Rectangle`.

# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height
# def total_area(rectangles):
#     return sum(rectangle.calculate_area() for rectangle in rectangles)

# num_rectangles = int(input("Enter the number of rectangles: "))
# rectangles = []
# for i in range(num_rectangles):
#     width = float(input(f"Enter the width of rectangle {i + 1}: "))
#     height = float(input(f"Enter the height of rectangle {i + 1}: "))
#     rectangles.append(Rectangle(width, height))
# total = total_area(rectangles)
# print(f"The total area of {num_rectangles} rectangles is: {total}")

# 27. Create a class `BankAccount` with methods to deposit, withdraw, and display balance.

# class BankAccount:
#     def __init__(self, account_number, balance, owner_name):
#         self.account_number = account_number
#         self.balance = balance
#         self.owner_name = owner_name
    
#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             print(f"Deposited ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
#         else:
#             print( "Invalid deposit amount.")
    
#     def withdraw(self, amount):
#         overdraft_limit = -1000  # Example overdraft limit
#         if amount > 0:
#             if self.balance - amount >= overdraft_limit:
#                 self.balance -= amount
#                 print( f"Withdrew ₹{amount:.2f}. New balance: ₹{self.balance:.2f}")
#             else:
#                 print( "Withdrawal amount exceeds overdraft limit.")
#         else:
#             print("Invalid withdrawal amount.")
    
#     def check_balance(self):
#         print( f"Account balance for {self.owner_name}: ₹{self.balance}")

# # Example usage
# account = BankAccount(account_number="", balance=100000, owner_name="Rohan")
# account.check_balance()
# account.deposit(500)
# account.withdraw(200)
# account.withdraw(1800)
# account.check_balance()

# 28. Implement a program that simulates a simple library system using classes `Book` and `Library`.

# class Book:
#     def __init__(self, title, author, book_id):
#         self.title = title
#         self.author = author
#         self.book_id = book_id
#         self.is_checked_out = False

#     def checkout(self):
#         if not self.is_checked_out:
#             self.is_checked_out = True
#             return True
#         else:
#             return False

#     def checkin(self):
#         if self.is_checked_out:
#             self.is_checked_out = False
#             return True
#         else:
#             return False

#     def __str__(self):
#         return f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Checked Out: {self.is_checked_out}"

# class Library:
#     def __init__(self):
#         self.books = {}

#     def add_book(self, book):
#         self.books[book.book_id] = book

#     def remove_book(self, book_id):
#         if book_id in self.books:
#             del self.books[book_id]
#             print(f"Book with ID {book_id} has been removed.")
#         else:
#             print(f"Book with ID {book_id} not found in the library.")

#     def display_books(self):
#         for book in self.books.values():
#             print(book)

# # Create library instance
# library = Library()

# # Add books to the library
# book1 = Book("The Catcher in the Rye", "J.D. Salinger", 1)
# book2 = Book("To Kill a Mockingbird", "Harper Lee", 2)
# book3 = Book("1984", "George Orwell", 3)

# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)

# # Display all books in the library
# print("Books in the library:")
# library.display_books()

# # Checkout a book
# book_id_to_checkout = 2
# book_to_checkout = library.books.get(book_id_to_checkout)
# if book_to_checkout and book_to_checkout.checkout():
#     print(f"Book {book_to_checkout.title} has been checked out.")
# else:
#     print(f"Book {book_id_to_checkout} is not available or already checked out.")

# # Display updated book status
# print("\nUpdated book status:")
# library.display_books()

# # Checkin a book
# book_id_to_checkin = 2
# book_to_checkin = library.books.get(book_id_to_checkin)
# if book_to_checkin and book_to_checkin.checkin():
#     print(f"Book {book_to_checkin.title} has been checked in.")
# else:
#     print(f"Book {book_id_to_checkin} cannot be checked in.")

# # Display updated book status
# print("\nUpdated book status:")
# library.display_books()


# 29. Develop a class `Employee` with attributes: name, position, and salary. Implement methods to give raises and display details.

# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary

#     def give_raise(self, amount):
#         if amount > 0:
#             self.salary += amount
#             print(f"{self.name} received a raise of ₹{amount}. New salary: ₹{self.salary}")
#         else:
#             print("Invalid raise amount.")

#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Position: {self.position}")
#         print(f"Salary: ₹{self.salary}")

# # Create an Employee instance
# employee1 = Employee("John Doe", "Manager", 50000)

# # Display employee details
# print("Employee Details:")
# employee1.display_details()

# # Give a raise to the employee
# employee1.give_raise(5000)

# # Display updated employee details
# print("\nUpdated Employee Details:")
# employee1.display_details()


# 30. Write a program that implements a basic calculator using a class `Calculator`.

# class Calculator:
#     def add(self, num1, num2):
#         return num1 + num2

#     def subtract(self, num1, num2):
#         return num1 - num2

#     def multiply(self, num1, num2):
#         return num1 * num2

#     def divide(self, num1, num2):
#         if num2 == 0:
#             return "Cannot divide by zero"
#         else:
#             return num1 / num2

# # Create a Calculator instance
# calculator = Calculator()

# # Menu for the calculator
# print("Basic Calculator Menu:")
# print("1. Addition")
# print("2. Subtraction")
# print("3. Multiplication")
# print("4. Division")
# choice = int(input("Enter your choice (1/2/3/4): "))

# # Get user input for numbers
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))

# # Perform the selected operation
# if choice == 1:
#     result = calculator.add(num1, num2)
#     operation = "Addition"
# elif choice == 2:
#     result = calculator.subtract(num1, num2)
#     operation = "Subtraction"
# elif choice == 3:
#     result = calculator.multiply(num1, num2)
#     operation = "Multiplication"
# elif choice == 4:
#     result = calculator.divide(num1, num2)
#     operation = "Division"
# else:
#     result = "Invalid Choice"
#     operation = "N/A"

# # Display the result
# print(f"{operation} Result: {result}")



# 31. Create a class hierarchy for different types of vehicles (car, bike, truck) with common and specific attributes.

# class Vehicle:
#     def __init__(self, make, model, year, color):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.color = color
#         self.is_running = False

#     def start(self):
#         self.is_running = True
#         print(f"The {self.color} {self.make} {self.model} has started.")

#     def stop(self):
#         self.is_running = False
#         print(f"The {self.color} {self.make} {self.model} has stopped.")

#     def honk(self):
#         print("Honk! Honk!")

# class Car(Vehicle):
#     def __init__(self, make, model, year, color, num_doors):
#         super().__init__(make, model, year, color)
#         self.num_doors = num_doors

#     def show_details(self):
#         print(f"Car Details - Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Number of Doors: {self.num_doors}")

# class Bike(Vehicle):
#     def __init__(self, make, model, year, color, num_gears):
#         super().__init__(make, model, year, color)
#         self.num_gears = num_gears

#     def show_details(self):
#         print(f"Bike Details - Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Number of Gears: {self.num_gears}")

# class Truck(Vehicle):
#     def __init__(self, make, model, year, color, max_load):
#         super().__init__(make, model, year, color)
#         self.max_load = max_load

#     def show_details(self):
#         print(f"Truck Details - Make: {self.make}, Model: {self.model}, Year: {self.year}, Color: {self.color}, Maximum Load Capacity: {self.max_load} tons")

# # Create instances of each vehicle type
# car1 = Car("Toyota", "Camry", 2022, "Blue", 4)
# bike1 = Bike("Honda", "CBR500R", 2021, "Red", 6)
# truck1 = Truck("Ford", "F-150", 2020, "White", 2.5)

# # Start and stop some vehicles
# car1.start()
# car1.stop()

# bike1.start()
# bike1.stop()

# truck1.start()
# truck1.stop()

# # Display vehicle details
# car1.show_details()
# bike1.show_details()
# truck1.show_details()


# 32. Implement a program that models a basic online shopping system using classes `Product` and `Cart`.

# class Product:
#     def __init__(self, product_id, name, price):
#         self.product_id = product_id
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f"{self.name} - ${self.price:.2f}"

# class Cart:
#     def __init__(self):
#         self.items = []

#     def add_to_cart(self, product, quantity):
#         self.items.append((product, quantity))
#         print(f"{quantity} {product.name}(s) added to the cart.")

#     def remove_from_cart(self, product, quantity):
#         for item in self.items:
#             if item[0] == product:
#                 if item[1] >= quantity:
#                     item = (item[0], item[1] - quantity)
#                     print(f"{quantity} {product.name}(s) removed from the cart.")
#                     return
#                 else:
#                     print(f"Error: Not enough {product.name}(s) in the cart to remove.")
#                     return
#         print(f"Error: {product.name} not found in the cart.")

#     def view_cart(self):
#         if not self.items:
#             print("Your cart is empty.")
#         else:
#             print("Your Cart:")
#             total_price = 0
#             for item in self.items:
#                 product, quantity = item
#                 subtotal = product.price * quantity
#                 total_price += subtotal
#                 print(f"{product.name} x{quantity}: ${subtotal:.2f}")
#             print(f"Total Price: ${total_price:.2f}")

# # Create some products
# product1 = Product(1, "Laptop", 999.99)
# product2 = Product(2, "Headphones", 49.99)
# product3 = Product(3, "Mouse", 19.99)

# # Create a cart
# cart = Cart()

# # Add products to the cart
# cart.add_to_cart(product1, 2)
# cart.add_to_cart(product2, 1)
# cart.add_to_cart(product3, 3)

# # View the cart
# cart.view_cart()

# # Remove products from the cart
# cart.remove_from_cart(product1, 1)
# cart.remove_from_cart(product2, 2)

# # View the updated cart
# cart.view_cart()

# 33. Develop a class hierarchy for a zoo with different types of animals, each having specific attributes and methods.

# class Animal:
#     def __init__(self, name, species, age):
#         self.name = name
#         self.species = species
#         self.age = age

#     def make_sound(self):
#         pass  # Specific animals will override this method

#     def eat(self, food):
#         print(f"{self.name} is eating {food}")

#     def sleep(self):
#         print(f"{self.name} is sleeping")

# class Mammal(Animal):
#     def give_birth(self):
#         print(f"{self.name} is giving birth to live young")

# class Bird(Animal):
#     def lay_eggs(self):
#         print(f"{self.name} is laying eggs")

# class Reptile(Animal):
#     def lay_eggs(self):
#         print(f"{self.name} is laying eggs")

# class Lion(Mammal):
#     def make_sound(self):
#         print(f"{self.name} roars")

# class Elephant(Mammal):
#     def make_sound(self):
#         print(f"{self.name} trumpets")

# class Parrot(Bird):
#     def make_sound(self):
#         print(f"{self.name} squawks")

# class Snake(Reptile):
#     def make_sound(self):
#         print(f"{self.name} hisses")

# # Create instances of different animals
# lion = Lion("Simba", "Lion", 5)
# elephant = Elephant("Dumbo", "Elephant", 8)
# parrot = Parrot("Polly", "Parrot", 2)
# snake = Snake("Slytherin", "Snake", 3)

# # Interact with the animals
# lion.make_sound()
# lion.eat("meat")
# lion.sleep()
# lion.give_birth()

# elephant.make_sound()
# elephant.eat("plants")
# elephant.sleep()
# elephant.give_birth()

# parrot.make_sound()
# parrot.eat("seeds")
# parrot.sleep()
# parrot.lay_eggs()

# snake.make_sound()
# snake.eat("mice")
# snake.sleep()
# snake.lay_eggs()


# 34. Create a text-based adventure game with classes `Player`, `Enemy`, and `Game`.

# 35. Implement a simple banking system with classes `Account`, `SavingsAccount`, and `CurrentAccount`.

# 36. Develop a class `Student` with attributes: name, age, and a list of subjects. Implement methods to calculate GPA and display details.

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.subjects = {}

#     def add_subject(self, subject, grade):
#         self.subjects[subject] = grade

#     def calculate_gpa(self):
#         if not self.subjects:
#             return 0.0  # No subjects, so GPA is 0
#         total_points = 0
#         total_credits = 0
#         for grade in self.subjects.values():
#             if grade in {"A", "a"}:
#                 points = 4.0
#             elif grade in {"B", "b"}:
#                 points = 3.0
#             elif grade in {"C", "c"}:
#                 points = 2.0
#             elif grade in {"D", "d"}:
#                 points = 1.0
#             else:
#                 points = 0.0
#             total_points += points
#             total_credits += 1
#         return total_points / total_credits

#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print("Subjects and Grades:")
#         for subject, grade in self.subjects.items():
#             print(f"{subject}: {grade}")
#         gpa = self.calculate_gpa()
#         print(f"GPA: {gpa:.2f}")

# # Create a Student instance
# student1 = Student("John Doe", 20)

# # Add subjects and grades
# student1.add_subject("Math", "A")
# student1.add_subject("English", "B")
# student1.add_subject("Science", "A")

# # Display student details
# student1.display_details()

# 37. Write a program to manage a movie database using classes `Movie` and `MovieDatabase`.

# 38. Create a class hierarchy for various electronic devices (phone, laptop, tablet) with common and specific features.

# 39. Implement a program that models a basic inventory system using classes `Product` and `Inventory`.