#Give any input and display its freq 
def char_frequency(s):
    counted = [] 
    for i in s:
        if i not in counted:
            count = 0
            for j in s:
                if i == j:
                    count += 1
            print(f"{i}{count}", end="")  
            counted.append(i)
char_frequency("ashritha")


    