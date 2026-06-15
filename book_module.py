books = []

def add_book(book_id, title):
    books.append({"id": book_id, "title": title, "available": True})
    print("Book added!")

def view_books():
    if not books:
        print("No books available.")
    for b in books:
        print(b)
