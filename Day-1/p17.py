#divisible by 5 and 11 or not
def div(x):
    if(x%5==0 and x%11==0):
        print('Given number is divisible by 5 and 11')
    else:
        print('Given number is not divisible by 5 and 11')
print(div(66))