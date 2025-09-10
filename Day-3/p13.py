#count total number of words in a string
def words(n):
    count=0
    for i in n:
        if(i==' '):
            count+=1
    print("total no of words",count+1)
words("I am Ashritha")
