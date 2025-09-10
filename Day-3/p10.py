#length of string
def string(n,n1):
    count=0
    count1=0
    for i in n:
        count+=1
    print(count)
    for i in n1:
        count1+=1
    print(count1)
    if(n==n1):
        print("Strings are same")
    else:
        print("Strings are not same")
    a=n+n1
    print("Concatenation",a)

string("Ash","ritha")