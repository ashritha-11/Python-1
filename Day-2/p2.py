#program to input anyb character and cj=heck whether it is alphabet,digit or special character
def func(char):
    if('a'<= char <= 'z') or ('A' <= char <= 'Z'):
        print(char,'is an alphabet')
    elif('0'<= char <='9'):
        print(char,'is a digit')
    elif char in ['@','#','/','?']:
        print(char,'is a special character')
    else:
        print("invalid input")
func('s')
func('8')
func('@')

