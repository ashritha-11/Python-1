from config import sb

def borrow_book(member_id, book_id):
    # Check stock
    book = sb.table("books").select("stock").eq("book_id", book_id).single().execute()
    if not book.data or book.data["stock"] <= 0:
        return {"error": "Book not available"}

    sb.table("books").update({"stock": book.data["stock"] - 1}).eq("book_id", book_id).execute()
    return sb.table("borrow_records").insert({"member_id": member_id, "book_id": book_id}).execute()

if __name__ == "__main__":
    mid = int(input("Member ID: "))
    bid = int(input("Book ID: "))
    print(borrow_book(mid, bid))
