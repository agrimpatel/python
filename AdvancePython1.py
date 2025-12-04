#WALRUS OPERATOR:It allows to assign values to variable as the part of an expression
"""if (n := len([1,2,3,4,5,6]))>3:
    print(f"List is too long ({n} elements,expected <= 3)")"""
    
#TYPES DEFINITIONS IN PYTHON
"""from typing import List,Union,tuple,dict
n : int = 5

name: str = "Agrim"

def sum(a: int,b: int)-> int:
    return a+b

sum(3,5)"""

#MATCH CASE(just like switch case)
"""def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "NOT FOOD"
        case 500:
            return "INTERNAL SERVER ERROR"
        case _:
            return "UNKNOWN STATUS"
        
        
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(403))"""

#DICTIONARY MERGE & UPDATE OPERATORS
"""dict1 = {'a':1,'b':2}
dict2 = {'b':3,'c':4}
merged = dict1 | dict2
print(merged)"""

#USE MULTIPLE CONTEXT MANAGERS IN A SINGLE "with" STATEMENT
"""with(
    open("file1.txt") as f1,
    open("file2.txt") as f2
):"""

#EXCEPTION HANDLING IN PYTHON
"""try:
    a = int(input("Hey,Enter a number:"))
    print(a)
    
except ValueError as v:
    print("Heyyy")
    print(v)
    
except Exception as e:
    print(e)
    
print("Thankyou")"""

#Raising Exception
"""a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if(b == 0):
    raise ZeroDivisionError("Hey,our program is not meant to divide bumbers by zero")
else:
    print(f"The division a/b is:{a/b}")"""
    
#Try with Else
"""try:
    a = int(input("Hey,Enter a number:"))
    print(a)
    
except Exception as e:
    print(e)
    
else:
    print("I am inside else")"""
    
#Try with Finally:It is basically used inside the function
"""def main():
    try:
        a = int(input("Hey,Enter a number:"))
        print(a)
    
    except Exception as e:
        print(e)
    
    finally:
        print("Hey,I am inside Finally")
        
main()"""   

#IF "__NAME__ == __MAIN__" IN PYTHON:HERE WE WILL IMPORT THE FUNCTION FROM ANOTHER FILE name Module
"""from Module import myFunct"""

#THE GLOBAL KEYWORD
"""a =89#Global variable
def fun():
    a =3#Global variable
    print(a)
    
fun()
print(a)"""

#ENUMERATION IN PYTHON
l = [3,513,52,535]
#This is alternate of the enumeration
#index = 0
#for item in l:
#   index  += 1
#   print(f"The item number {index} is : {item}")

#Enumeration
"""for index, item in enumerate(l):
    print(f"The item number at index {index} is {item}")"""
    
#LIST COMPREHENSIONS
myList = [1,2,3,5,6,5]

#squaredList = []
#for item in myList:
#   squaredList.append(item*item)

squaredList = [i*i for i in myList]
    
print(squaredList)
    


 



                
        
       
        
        
    
       