# calculator program using OOPS
class calculator:

    def addition(self,x,y):
        return x + y

    def subtraction(self,x,y):
        return x - y

    def multiplication(self,x,y):
        return x * y

    def division(self,x,y):
        return x / y

result = calculator()

while True:
    print("<< Select operator >>")
    print("+.addition")
    print("-.subtraction")
    print("*.multiplication")
    print("/.division")
    print("..close")

    x = float(input("Enter a First Number : "))
    y = float(input("Enter a Second Number : "))
    operator = input("Select Operator : ")
    

    if operator in ( "+", "-", "*", "/", "."):
        if (operator == "."):
            break

        if (operator == '+'):
            print(x, "+", y, "=", result.addition(x,y))
        
        elif (operator == '-'):
            print(x, "-", y, "=", result.subtraction(x,y))
        
        elif (operator == '*'):
            print(x, "*", y, "=", result.multiplication(x,y))
        
        elif (operator == '/'):
            print(x, "/", y, "=", result.division(x,y))
        

    else:
        print("Invalid Input")






