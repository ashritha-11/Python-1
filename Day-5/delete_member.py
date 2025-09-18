from config import sb

def delete_member(member_id):
    borrowed = sb.table("borrow_records").select("*").eq("member_id", member_id).is_("return_date", None).execute()
    if borrowed.data:
        return {"error": "Member still has borrowed books!"}
    return sb.table("members").delete().eq("member_id", member_id).execute()

if __name__ == "__main__":
    mid = int(input("Member ID to delete: "))
    print(delete_member(mid))
