class Book:
    def __init__(self, title, author, isbn, available_copies):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = available_copies

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print(f"Available Copies: {self.available_copies}\n")


class Patron:
    def __init__(self, name, library_card_number):
        self.name = name
        self.library_card_number = library_card_number
        self.borrowed_books = []

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Library Card Number: {self.library_card_number}")
        print("Borrowed Books:")
        for book in self.borrowed_books:
            print(f"- {book.title}")
        print()


class Library:
    def __init__(self):
        self.books = []
        self.patrons = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully!\n")

    def add_patron(self, patron):
        self.patrons.append(patron)
        print("Patron added successfully!\n")

    def borrow_book(self, patron, book_title):
        for book in self.books:
            if book.title == book_title and book.available_copies > 0:
                book.available_copies -= 1
                patron.borrowed_books.append(book)
                print("Book borrowed successfully!\n")
                return
        print("Book not available for borrowing.\n")

    def return_book(self, patron, book_title):
        for book in patron.borrowed_books:
            if book.title == book_title:
                book.available_copies += 1
                patron.borrowed_books.remove(book)
                print("Book returned successfully!\n")
                return
        print("You haven't borrowed this book.\n")


def main():
    library = Library()

    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0", 5)
    book2 = Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4", 3)

    patron1 = Patron("John Doe", "12345")
    patron2 = Patron("Jane Smith", "54321")

    library.add_book(book1)
    library.add_book(book2)
    library.add_patron(patron1)
    library.add_patron(patron2)

    while True:
        print("1. Add Book")
        print("2. Add Patron")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            title = input("Enter book title: ")
            author = input("Enter author: ")
            isbn = input("Enter ISBN: ")
            available_copies = int(input("Enter available copies: "))
            new_book = Book(title, author, isbn, available_copies)
            library.add_book(new_book)

        elif choice == 2:
            name = input("Enter patron name: ")
            library_card_number = input("Enter library card number: ")
            new_patron = Patron(name, library_card_number)
            library.add_patron(new_patron)

        elif choice == 3:
            library_card_number = input("Enter patron's library card number: ")
            book_title = input("Enter book title to borrow: ")
            patron = next((p for p in library.patrons if p.library_card_number == library_card_number), None)
            if patron:
                library.borrow_book(patron, book_title)
            else:
                print("Patron not found.\n")

        elif choice == 4:
            library_card_number = input("Enter patron's library card number: ")
            book_title = input("Enter book title to return: ")
            patron = next((p for p in library.patrons if p.library_card_number == library_card_number), None)
            if patron:
                library.return_book(patron, book_title)
            else:
                print("Patron not found.\n")

        elif choice == 5:
            print("Thank you for using the Library Management System!")
            break

        else:
            print("Invalid choice. Please choose again.\n")    
main()