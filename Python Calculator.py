#Calculator
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mup(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
def moddiv(n1,n2):
    return n1%n2
def intdiv(n1,n2):
    return n1//n2
def pow(n1,n2):
    return n1**n2
Operations={
    "+":add,
    "-":sub,
    "*":mup,
    "/":div,
    "%":moddiv,
    "//":intdiv,
    "**":pow,
}
def Repeat_Operation():
    print(logo)
    num1 = float(input("Enter your first number : "))
    for i in  Operations:
        print(i)
    Should_Continue = True
    while Should_Continue:
        Operation_symbol=input("Pick an operation symbol : ")
        num2 = float(input("Enter next number : "))
        Calculated_function = Operations[Operation_symbol]
        answer = Calculated_function(num1,num2)
        print(f"{num1} {Operation_symbol} {num2} = {answer}")
        if input("Type 'y' to continue or 'n' to exit or to start new calculation : ")=="y":
            num1 = answer
        else:
            Should_Continue = False
            Repeat_Operation()
Repeat_Operation()
        
        
        
        