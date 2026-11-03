class Library:
    def __init__(self):
        self.books = []
    def add_book(self):
        book_id=int(input("Enter book id"))
        title = input("Enter book name: ")
        author=input("Enter author name")

        self.books.append({"name": title,"Book Id":book_id,"Author name":author,"available": True})
        print("Book added successfully")
    def issue_book(self):
        title = input("Enter book name to issue: ")
        for book in self.books:
            if book["name"] == title and book["available"]:
                book["available"] = False
                print("Book issued successfully")
            else:
                print("Book is alreadi issued")
            return
        print("Book not found")
    def return_book(self):
        title = input("Enter book name to return: ")
        for book in self.books:
            if book["name"] == title and book["available"]:
                book["available"] = True
                print("Book returned successfully")
            else:
                print("This book was not issued")
            return
            
        print("Book not found ")
    def display_books(self):
        for book in self.books:
            if book["available"]:
                print(book["name"])
library = Library()
while True:
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Display Books")
    print("5. Exit")
    choice = input("Enter choice: ")
    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.issue_book()
    elif choice == "3":
        library.return_book()
    elif choice == "4":
        library.display_books()
    elif choice == "5":
        break
    else:
        print("Invalid choice")