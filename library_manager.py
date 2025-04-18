import os
import json

# Book list
library = []

def display_menu():
    print("\nWelcome to your Personal Library Manager!")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Display statistics")
    print("6. Exit")


def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author: ")
    year = int(input("Enter the publication year: "))
    genre = input("Enter the genre: ")
    read_input = input("Have you read this book? (yes/no): ").strip().lower()
    read = True if read_input == "yes" else False

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(book)
    print(f"Book {title} added successfully!")


def remove_book():
    title = input("Enter the title of the book to remove: ")
    found = False
    for book in library:
        if book["title"].lower() == title.lower():
            library.remove(book)
            found = True
            print("Book removed successfully!")
            break
    if not found:
        print("Book not found.")


def search_book():
    print("Search by:\n1. Title\n2. Author")
    choice = input("Enter your choice: ")
    keyword = input("Enter the title/author: ").lower()
    results = []

    if choice == "1":
        results = [book for book in library if keyword in book["title"].lower()]
    elif choice == "2":
        results = [book for book in library if keyword in book["author"].lower()]
    else:
        print("Invalid choice.")
        return

    if results:
        print("Matching Books:")
        for idx, book in enumerate(results, 1):
            status = "Read" if book["read"] else "Unread"
            print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")
    else:
        print("No matching books found.")


def display_books():
    if not library:
        print("Library is empty.")
        return

    print("Your Library:")
    for idx, book in enumerate(library, 1):
        status = "Read" if book["read"] else "Unread"
        print(f"{idx}. {book['title']} by {book['author']} ({book['year']}) - {book['genre']} - {status}")


def display_stats():
    total = len(library)
    if total == 0:
        print("No books in the library.")
        return

    read_books = sum(1 for book in library if book["read"])
    percentage = (read_books / total) * 100
    print(f"Total books: {total}")
    print(f"Percentage read: {percentage:.1f}%")


def save_library():
    with open("library.txt", "w") as f:
        json.dump(library, f)

def load_library():
    if os.path.exists("library.txt"):
        with open("library.txt", "r") as f:
            global library
            library = json.load(f)

def main():
    load_library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            remove_book()
        elif choice == "3":
            search_book()
        elif choice == "4":
            display_books()
        elif choice == "5":
            display_stats()
        elif choice == "6":
            save_library()
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()