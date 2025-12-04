#Problem1
"""virtual environment problem"""

#Problem2
"""x = str(input("Enter the name:"))
y = int(input("Enter marks:"))
z = int(input("Enter the phone number:"))
a = "The name of the student is {}, his marks are {} and phone number is {}".format(x,y,z)
print(a)"""

#Problem3
"""table = [str(7*i) for i in range(1,11)]

s = "\n".join(table)
print(s)"""

#Problem4
"""l = [2,20,15,35,45,4,5,6,7,60]
def divisibleByFive(a):
    if(a%5 == 0):
        return True
    else:
        return False
    
d = filter(divisibleByFive,l)
print(list(d))"""

from functools import reduce
#Problem5
"""list = [3,4,67,7,6]
def greater(a,b):
    if(a>b):
        return a
    else:
        return b
    
print(reduce(greater,list))"""

#Problem6
"Run pip freeze for the system interpreter.Take the conytent and creat a similar virtualenv"""
"""pip freeze > requirements.txt
virtualenv harryenv"""

#Problem7
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello World!</p>" 

app.run()

 


