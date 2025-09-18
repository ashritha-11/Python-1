from config import sb

def update_member(member_id, new_email):
    return sb.table("members").update({"email": new_email}).eq("member_id", member_id).execute()

if __name__ == "__main__":
    mid = int(input("Member ID: "))
    email = input("New Email: ")
    print(update_member(mid, email).data)
