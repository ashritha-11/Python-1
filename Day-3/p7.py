#unique elements in a list
def unique_elements(lst):
    uniques = []  
    for i in range(len(lst)):
        count = 0
        for j in range(len(lst)):
            if lst[i] == lst[j]:
                count += 1
        if count == 1:   
            uniques.append(lst[i])
    
    return uniques


numbers = [1, 2, 2, 3, 4, 1, 5, 6, 4]
print("Unique elements:", unique_elements(numbers))
