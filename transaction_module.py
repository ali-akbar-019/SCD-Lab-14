from book_module import books

def borrow_book(book_id):
    for book in books:
        if book["id"] == book_id and book["available"]:
            book["available"] = False
            print("Book borrowed!")
            return
    print("Book not available.")

def return_book(book_id):
    for book in books:
        if book["id"] == book_id:
            book["available"] = True
            print("Book returned!")
            return
    print("Book not found.")
