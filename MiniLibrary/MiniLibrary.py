#ZE LIBRARY
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
class Library:
    books = []
    def __init__(self, other):
        self.books.append(other)

    def display_books(self):
        for i in self.books:
            print (i.title, "By", i.author)

    def remove_book(self, x_tit, x_auth):
        for bkks in self.books:
            if x_tit == bkks.title and x_auth == bkks.author:
                self.books.remove(bkks)
def main_menu():
    print("--------------")
    print("1. Show Books")
    print("2. Add Books")
    print("3. Remove Books")
    print("4. Quit")
def get_number(input_text):
    while True:
        try:
            num=int(input(input_text))
            return num
        except ValueError:
            print("Invalid Choice")
while True:
    main_menu()
    choice = get_number("Enter Your Choice: ")
    bk = Book(" ", " ")
    if choice == 1:
        try:
            lb.display_books()
        except NameError:
            print("No books yet")
    elif choice == 2:
        b_tit = input("Book Title: ")
        b_auth = input("Book Author: ")
        bk = Book(b_tit, b_auth)
        lb = Library(bk)
    elif choice == 3:
        a_tit = input("Book Title: ")
        a_auth = input("Book Author: ")
        lb.remove_book(a_tit,a_auth)
    elif choice == 4:
        break
    print (" ")