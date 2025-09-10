#add elements to an empty set and display them
def empty(n):
    s = set()
    for i in range(n):
        a = input("Enter a number: ")
        s.add(a)
    print("Set elements:", s)

empty(5)
