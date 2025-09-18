from config import sb

def update_book_stock(book_id, stock):
    return sb.table("books").update({"stock": stock}).eq("book_id", book_id).execute()

if __name__ == "__main__":
    bid = int(input("Book ID: "))
    stock = int(input("New Stock: "))
    print(update_book_stock(bid, stock).data)
