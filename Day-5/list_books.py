from config import sb

def list_books():
    return sb.table("books").select("*").execute()

if __name__ == "__main__":
    books = list_books().data
    for b in books:
        print(b)
