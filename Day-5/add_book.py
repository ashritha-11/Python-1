from config import sb

def add_book(title, author, category, stock=1):
    return sb.table("books").insert({"title": title, "author": author, "category": category, "stock": stock}).execute()

if __name__ == "__main__":
    title = input("Title: ")
    author = input("Author: ")
    category = input("Category: ")
    stock = int(input("Stock: "))
    print(add_book(title, author, category, stock).data)
