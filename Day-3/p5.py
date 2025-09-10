#delete element at a specified postion
def delete_at_position():
    lst = [10, 20, 30, 40, 50]
    pos = 2  
    if 0 <= pos < len(lst):
        for i in range(pos, len(lst) - 1):
            lst[i] = lst[i + 1]
        lst = lst[:-1]

        print("Updated list:", lst)
    else:
        print("Invalid position")

delete_at_position()


