from config import sb

def list_members():
    return sb.table("members").select("*").execute()

if __name__ == "__main__":
    members = list_members().data
    for m in members:
        print(m)
