#program to find highest freq char in a string
def high(n):
    n = n.lower()
    counted = []
    max_count = 0
    max_char = ''

    for i in n:
        if i not in counted:
            count = 0
            for j in n:
                if i == j:
                    count += 1
            if count > max_count:
                max_count = count
                max_char = i
            counted.append(i)

    print(f"Character with highest frequency: '{max_char}' occurs {max_count} times")
high("ashritha")

