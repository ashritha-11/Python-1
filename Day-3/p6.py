#find frequency of a list
def frequency(lst):
    visited = []   
    for i in range(len(lst)):
        already = False
        for k in range(len(visited)):
            if visited[k] == lst[i]:
                already = True
                break
        if not already:
            count = 0
            for j in range(len(lst)):
                if lst[i] == lst[j]:
                    count += 1
            print(lst[i], "occurs", count, "times")
            visited.append(lst[i])
numbers = [1, 2, 2, 3, 4, 1, 2, 4, 5]
frequency(numbers)

