#exception handling
def division():
    try:
         a=int(input("Enter numerator"))
         b=int(input("Enter denominator"))
         c=a/b
         if a>b or a<b:
             print(c)
    except ZeroDivisionError:
        print("Error:Division by zero is not allowed")
division()



   
