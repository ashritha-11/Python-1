def library_system():
    library = {}  
    while True:
        print(" Library Management System ")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search a book by ID")
        print("4. Update book title")
        print("5. Display all books")
        print("6. Count total books")
        print("7. Check if a book title exists")
        print("8. Exit")
        choice = input("Enter your choice (1-8): ")
        if choice == "1":
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            if book_id in library:
                print("Book ID already exists! Cannot add.")
            else:
                library[book_id] = title
                print(f"Book '{title}' added successfully.")
        elif choice == "2":
            book_id = input("Enter Book ID to remove: ")
            removed_title = library.pop(book_id, None)  
            if removed_title:
                print(f"Book '{removed_title}' removed successfully.")
            else:
                print("Book ID not found!")
        elif choice == "3":
            book_id = input("Enter Book ID to search: ")
            title = library.get(book_id)  
            if title:
                print(f"Book found: {title}")
            else:
                print("Book ID not found!")
        elif choice == "4":
            book_id = input("Enter Book ID to update: ")
            if book_id in library:
                new_title = input("Enter new title: ")
                library.update({book_id: new_title}) 
                print("Book title updated successfully.")
            else:
                print("Book ID not found!")
        elif choice == "5":
            if not library:
                print("Library is empty.")
            else:
                print("\nAll books in the library:")
                for bid, title in library.items(): 
                    print(f"ID: {bid} -> Title: {title}")
        elif choice == "6":
            print(f"Total number of books: {len(library)}")  
        elif choice == "7":
            title_check = input("Enter book title to check: ").lower()
            if any(title.lower() == title_check for title in library.values()):
                print("Book title exists in the library.")
            else:
                print("Book title does NOT exist.")
        elif choice == "8":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1-8.")
library_system()
