#program to find lowest freq char in a string
def lowest_freq(n):
    n = n.lower()  
    counted = []
    min_count = len(n) + 1  
    min_char = ''

    for i in n:
        if i not in counted:
            count = 0
            for j in n:
                if i == j:
                    count += 1
            if count < min_count:
                min_count = count
                min_char = i
            counted.append(i)

    print(f"Character with lowest frequency: '{min_char}' occurs {min_count} times")
lowest_freq("ashritha")


