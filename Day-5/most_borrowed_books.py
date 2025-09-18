from config import sb

def most_borrowed_books():
    return sb.table("most_borrowed_books").select("*").execute()

if __name__ == "__main__":
    books = most_borrowed_books().data
    for b in books:
        print(b)
