#1. Implement a class `Student` with attributes `name`, `roll_number`, and a dictionary of `subjects` and their `grades`. Add a method to calculate the GPA.

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

# 2. Implement a class `Student` with attributes `name`, `roll_number`, and a dictionary of `subjects` and their `grades`. Add a method to calculate the GPA.

# 3. Design a class `Library` with attributes `name`, a list of `books`, and a dictionary of `patrons` 
# and their `borrowed_books`. Implement methods to add a book, borrow a book, and return a book.
# class Library:
#     def __init__(self, name):
#         self.name = name
#         self.books = []
#         self.patrons = {}
    
#     def add_book(self, book_title, book_author):
#         book = {'title': book_title, 'author': book_author, 'available': True}
#         self.books.append(book)
#         return f"Book '{book_title}' by {book_author} added to the library."
    
#     def borrow_book(self, patron_name, book_title):
#         if patron_name in self.patrons and book_title in [book['title'] for book in self.books]:
#             patron = self.patrons[patron_name]
#             book = next((book for book in self.books if book['title'] == book_title), None)
            
#             if book['available']:
#                 book['available'] = False
#                 patron['borrowed_books'].append(book_title)
#                 return f"{patron_name} borrowed '{book_title}'."
#             else:
#                 return f"'{book_title}' is already borrowed by another patron."
#         else:
#             return "Patron not found or book not available in the library."
    
#     def return_book(self, patron_name, book_title):
#         if patron_name in self.patrons:
#             patron = self.patrons[patron_name]
#             if book_title in patron['borrowed_books']:
#                 book = next((book for book in self.books if book['title'] == book_title), None)
#                 book['available'] = True
#                 patron['borrowed_books'].remove(book_title)
#                 return f"{patron_name} returned '{book_title}'."
#             else:
#                 return f"'{book_title}' is not borrowed by {patron_name}."
#         else:
#             return "Patron not found."
    
#     def add_patron(self, patron_name):
#         self.patrons[patron_name] = {'borrowed_books': []}
#         return f"{patron_name} has been added to the list of patrons."
    
#     def list_books(self):
#         book_list = [f"'{book['title']}' by {book['author']} (Available: {book['available']})" for book in self.books]
#         return "\n".join(book_list)
    
#     def list_patrons(self):
#         patron_list = [f"{patron}: {', '.join(patron_data['borrowed_books'])}" for patron, patron_data in self.patrons.items()]
#         return "\n".join(patron_list)

# # Example usage
# library = Library(name="My Library")
# library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
# library.add_book("To Kill a Mockingbird", "Harper Lee")
# library.add_book("1984", "George Orwell")
# library.add_patron("Alice")
# library.add_patron("Bob")
# print(library.list_books())
# print(library.list_patrons())
# library.borrow_book("Alice", "The Great Gatsby")
# library.borrow_book("Bob", "To Kill a Mockingbird")
# print(library.list_books())
# print(library.list_patrons())
# library.return_book("Alice", "The Great Gatsby")
# print(library.list_books())
# print(library.list_patrons())

# 4. Create a class `Polygon` with an attribute `sides`. Implement a method to calculate the perimeter. Derive classes `Triangle`, `Rectangle`, and `Pentagon` with methods to calculate area.

# 5. Implement a class `Contact` with attributes `name`, `email`, and `phone_number`. Derive classes `Friend` and `Colleague`. Add methods specific to each subclass.

# *Inheritance:*

# 6. Define a class `Vehicle` with attributes `make`, `model`, and `year`. Derive classes `Car` and `Motorcycle`. Implement a method to check if a vehicle is a luxury vehicle (e.g., based on price or features).


# 7. Create a class `Shape` with attributes `sides` and `color`. Derive classes `Triangle`, `Rectangle`, and `Pentagon`. Add a method to check if a shape is regular (all sides and angles equal).

# 8. Design a class `BankAccount` with attributes `account_number`, `balance`, and `owner_name`. Implement a method for transferring money between accounts, considering different account types.

# 9. Implement a class `UniversityMember` with attributes `name` and `role`. Derive classes `Student` and `Professor`. Add a method to calculate the years of experience for professors.

# 10. Create a class `StoreItem` with attributes `name`, `price`, and `quantity`. Derive classes `PerishableItem` and `NonPerishableItem`. Implement methods to calculate total value considering shelf life for perishable items.