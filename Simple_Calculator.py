a= int(input("enter the no 1: "))
b= int(input("enter no 2: "))
print ( " enter + to add")
print ( " enter - to substract")
print ( " enter * to multiply")
print ( " enter / to divide")
print ( " enter . to exit")

ans = 0
def add():
    ans=a+b
    print(ans)

def sub():
    ans = a-b
    print(ans)

def product():
    ans = a * b 
    print(ans)

def divide():
    ans = a//b 
    print(ans)

while True:
    choice= input (" enter your choice") # + 
    if choice == "+":
        #print( a+ b) optionone
        add()
    elif choice == "-":
        sub()
    elif choice == "*":
        product()
    elif choice == "/":
        divide()
    elif choice == ".":
        break
    else:
        print("enter the correct choice")