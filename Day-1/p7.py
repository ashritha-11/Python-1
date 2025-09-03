#Student details
a=int(input('Enter student number'))
b=input('Enter student name')
c,d,e=map(int,input('Three subjects marks').split())
avg=(c+d+e)/3
print(a)
print(b)
print(round(avg,2))
  