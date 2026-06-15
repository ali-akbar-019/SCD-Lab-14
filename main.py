from user_module import add_user, view_users
from book_module import add_book, view_books
from transaction_module import borrow_book, return_book

def menu():
    while True:
        print("\n--- Library System ---")
        print("1. Add User")
        print("2. View Users")
        print("3. Add Book")
        print("4. View Books")
        print("5. Borrow Book")
        print("6. Return Book")
        print("0. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            uid = input("User ID: ")
            name = input("Name: ")
            add_user(uid, name)

        elif choice == "2":
            view_users()

        elif choice == "3":
            bid = input("Book ID: ")
            title = input("Title: ")
            add_book(bid, title)

        elif choice == "4":
            view_books()

        elif choice == "5":
            bid = input("Book ID to borrow: ")
            borrow_book(bid)

        elif choice == "6":
            bid = input("Book ID to return: ")
            return_book(bid)

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

menu()
