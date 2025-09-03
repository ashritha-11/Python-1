#Greatest of three numbers
def great(a,b,c):
    if(a>b):
        if(a>c):
            print(a,'is the greatest')
        else:
            print(c,'is the greatest')
    elif(b>a):
        if(b>c):
            print(b,'is the greatest')
        else:
            print(c,'is the greatest')
    else:
        print(c,'is the greatest')
print(great(2,5,10))
