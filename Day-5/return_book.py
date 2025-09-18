from config import sb

def return_book(record_id):
    record = sb.table("borrow_records").select("*").eq("record_id", record_id).single().execute()
    if not record.data or record.data["return_date"]:
        return {"error": "Invalid record or already returned"}

    book_id = record.data["book_id"]
    stock = sb.table("books").select("stock").eq("book_id", book_id).single().execute().data["stock"]

    sb.table("books").update({"stock": stock + 1}).eq("book_id", book_id).execute()
    return sb.table("borrow_records").update({"return_date": "now()"}).eq("record_id", record_id).execute()

if __name__ == "__main__":
    rid = int(input("Borrow Record ID: "))
    print(return_book(rid))
