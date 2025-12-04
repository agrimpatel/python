#string
#Q1 
str = input("Enter First name:")
result = len(str)
print("The length of the strring is:",result)
#Q2
str = "I have $ and I want to spend all in buying a car"
count = 0
result2 = str.count("$")
print("The frequency is:", result2)

#Conditional 
#Q1
num = int(input("Enter the number:"))
if(num%2==0):
    print("Number is even.")
else:
    print("Number is odd.")    
#Q2
a = int(input("Enter number1: "))    
b = int(input("Enter number2: "))  
c = int(input("Enter number3: "))  
if(a>b and a>c):
     print("a is greater")
elif(b>a and b>c):
    print("b is greater")  
else:
    print("c is greater")   
#Q3
number = int(input("Enter the number:"))
if(number%7):
    print("Number is multiple of 7")
else:
    print("Any other number")    
         
