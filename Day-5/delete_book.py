from config import sb

def delete_book(book_id):
    borrowed = sb.table("borrow_records").select("*").eq("book_id", book_id).is_("return_date", None).execute()
    if borrowed.data:
        return {"error": "Book is currently borrowed!"}
    return sb.table("books").delete().eq("book_id", book_id).execute()

if __name__ == "__main__":
    bid = int(input("Book ID to delete: "))
    print(delete_book(bid))
