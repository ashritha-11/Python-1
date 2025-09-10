#program to count total no of even and odd elements in a list
def evenOdd():
    lst=[1,2,3,4,5,6]
    even_count=0
    odd_count=0
    for i in lst:
        if(i%2==0):
            even_count+=1
        else:
            odd_count+=1
    print("Even count",even_count)
    print("Odd count",odd_count)
evenOdd()

            

