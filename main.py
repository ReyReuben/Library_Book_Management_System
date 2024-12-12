from library import Library
from book import Book

def main():
    library = Library()

    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book by Title")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            year = int(input("Enter year of publication: "))
            isbn = input("Enter book ISBN: ")
            pages = int(input("Enter number of pages: "))
            book = Book(title, author, year, isbn, pages)
            library.add_book(book)
        elif choice == '2':
            library.display_books()
        elif choice == '3':
            title = input("Enter title to search: ")
            library.search_by_title(title)
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
