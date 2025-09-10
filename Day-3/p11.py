#program to find total no of alphabets,digits or special characters in a string
def string(n):
    count=0
    count1=0
    for i in n:
        if i.isalpha():
            count+=1
           
        elif i.isdigit():
            count1+=1
    print("Alphabet",count)
    print("Digit",count1)
string("ash123")
