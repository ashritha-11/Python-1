#Student pass or fail
def stu(marks):
    if(marks>80):
        print('Distension')
    elif(71<=marks<=80):
        print('A')
    elif(51<=marks<=70):
        print('B')
    elif(40<=marks<=50):
        print('C')
    else:
        print('Fail')
stu(80)
