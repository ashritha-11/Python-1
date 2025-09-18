from config import sb

def add_member(name, email):
    return sb.table("members").insert({"name": name, "email": email}).execute()

if __name__ == "__main__":
    name = input("Enter member name: ")
    email = input("Enter email: ")
    print(add_member(name, email).data)
