#Function wihtout arguments
def funct():
    print("Hello")
    
    
funct()
print("Good day")
funct()


def avg():
    a = int(input("Enter first number:"))
    b = int(input("Enter second number:"))
    c = int(input("Enter third number:"))
    
    average = (a+b+c)/3
    print(average)
    
avg()#Function call


#Function with arguments
def goodday(name):
    print(" Good day " + name)
    
goodday("Agrim")

#Default Argument
def goodday(name , ending="Thank you"):
    print(f"Good Day, {name}")
    print(ending)
    
goodday("Agrim")
    