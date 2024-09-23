class Book:
    def __init__(self, title, author, borrower, status):
        self.title = title
        self.author = author
        self.borrower = borrower
        self.status = status

#data of the book
b_1 = Book("1984", "George Orwell", "Alice", "Borrowed")
b_2 = Book("To Kill a Mockingbird", "Harper Lee", "Charlie", "Borrowed")
b_3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "", "Available")
b_4 = Book("War and Peace", "Leo Tolstoy", "Alice", "Borrowed")
b_5 = Book("Pride and Prejudice", "Jane Austen", "Diana", "Borrowed")
b_6 = Book("Brave New World", "Aldous Huxley", "", "Available")
b_7 = Book("The Catcher in the Rye", "J.D. Salinger", "Bob", "Borrowed")
b_8 = Book("Crime and Punishment", "Fyodor Dostoevsky", "Eve", "Borrowed")
b_9 = Book("The Lord of the Rings", "J.R.R. Tolkien", "Charlie", "Borrowed")
b_10 = Book("The Hobbit", "J.R.R. Tolkien", "Charlie", "Borrowed")

#displaying the information needed
print("Books borrowed by Alice:")
print(b_1.title, "by", b_1.author)#first book
print(b_4.title, "by", b_4.author)#second book

#available book
print("\nBooks that are available:")
print(b_3.title, "by", b_3.author)#The Great Gatsby
print(b_6.title, "by", b_6.author)#Brave New World

print("\nBooks by J.R.R. Tolkien and Jane Austen:")
print(b_5.title, "/ Borrower:", b_5.borrower, "/ Status:", b_5.status)  # Pride and Prejudice
print(b_9.title, "/ Borrower:", b_9.borrower, "/ Status:", b_9.status)  # The Lord of the Rings
print(b_10.title, "/ Borrower:", b_10.borrower, "/ Status:", b_10.status)  # The Hobbit

#Sir paawat ka naman please T_T; AHAHAHAHAHA