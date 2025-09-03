#current bill and total units
a=int(input('Enter customer number'))
b=input('Enter customer name')
pmr=float(input('Enter present month reading'))
lmr=float(input('Enter last month reading'))
tu=pmr-lmr
cbill=tu*3.80
print('Customer number',a)
print('Customer name',b)
print('Total units',tu) 
print('Current bill',cbill) 
print(f"Customer number {a}\n Customer name {b}\n Total units {tu}\n Current bill {cbill}")