#VIRTUAL ENVIRONMENT

# >Installation:
#>>>> pip install virtualenv(on terminal)
#To activate virtual environment:give command(.\env\Scripts\activate.ps1)

#To create a new virtual environment:(virtual myprojectenv) 

#PIP FREEZE COMMAND:it returns all the packages installed in a given  python environment along with the versions
#>>>(pip freeze > requirements.txt):It creates a file named 'requirements.txt' in the same folder cantaining the o/p of 'pip freeze'

#LAMBDA FUNCTIONS:It is shortcut to define a functions in single line
#@Example1
"""square = lambda a:a*a
square(5)"""

#@Example2
"""sum = lambda a,b,c:a+b+c
sum(2,3,4)"""

#JOIN METHOD(STRINGS)
"""a = ["Agrim","Rohan","Shubham","Sonu"]

final = "::".join(a)#It will join sll elements of the list by "::"
print(final)"""

#FORMATE METHOD(STRINGS)
"""a = "{} is a good {}".format("Agrim","Boy")
print(a)"""

#MAP,FILTER AND REDUCE
#Map ex
"""l = [1,2,3,4,5]
square = lambda x:x*x

sqList = map(square,l)
print(list(sqList))"""

#Filter ex
"""l = [1,2,3,4,5]
def even(n):
    if(n%2 == 0):
        return True
    else:
        return False

onlyList = filter(even,l) 
print(list(onlyList))"""

from functools import reduce
#Reduce 
#@Ex1
"""l = [1,2,3,4,5]
def sum(a,b):
    return a+b

print(reduce(sum,l))"""

#@Ex2
"""mul = lambda a,b:a*b
print(reduce(mul,l))"""











