def cart():
    lst = input("Enter numbers separated by space: ").split()
    print("Initial List:", lst)

    if len(lst) < 3:
        a = input("Element to add: ")
        lst.append(a)
        print("Updated List (after adding):", lst)

    elif len(lst) > 10:
        removed = lst[-1]   
        lst.pop()
        print("Removed element:", removed)
        print("Updated List (after removal):", lst)

    elif len(lst) == 10:
        print("Cart has 10 items:")
        for item in lst:
            print(item, end=" ")
        print()

    elif 3 <= len(lst) < 10:
        b = input("Element to search: ")
        found = False
        for item in lst:  
            if item == b:
                found = True
                break
        if found:
            print("Product found in the list")
        else:
            print("Product not found")
        print("Current List Elements:", lst)
    elif 3<len(lst)<=10:
        lst.sort()
        print(lst)
    elif 11<len(lst)<2:
        lst.clear()
        print(lst)


cart()
