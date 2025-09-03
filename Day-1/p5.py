#find simple interest and total amount
a=int(input('Enter principle amount'))
b=int(input('Enter rate of interest'))
c=int(input('Enter total no of months'))
SI=(a *b *c)/100
print('Simple interest is',SI)
TA=a+SI
print('Total amount is',TA)