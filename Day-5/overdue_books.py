from config import sb

def overdue_books():
    return sb.table("borrow_records").select("*, members(name), books(title)").is_("return_date", None).execute()

if __name__ == "__main__":
    recs = overdue_books().data
    for r in recs:
        print(r)
