#CLASSES and OBJECT
"""class Student:#Creating Class
    name = "Agrim"
    
s1 = Student()#Creating Object  
print(s1.name)"""

"""class Car:
    insurance  = "LIC"#Class Attribute it is common to all constructors
    
    def __init__(self):#Default constructor
        pass
    
    def __init__(self,colour,Brand):# Parametrized Constructor
        self.colour = colour
        self.Brand = Brand
        print("Adding new car in database...")
    
car1 = Car("Blue","BMW")#Object created and invoked
print(car1.colour,car1.Brand)

car2 = Car("Black","Mercedes")
print(car2.colour,car2.Brand)"""


#Methods in oops: they are present in class
"""class Car1:
    #Car stoped 
    def __init__(self):
    self.brake = True
    self.clutch = False
    self.Acc = False
    
    def strt(self):#Method to start the car
        self.brake = False
        self.clutch = True
        self.Acc = True
        print("Car started..")
        
car = Car1()
car.strt()"""
#EXAMPLE@
"""class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    @staticmethod #decorator
    def greet():#here, no need to write self as parametre
        print("Hello")
        
    def Avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(self.name, "your avg score is:",sum/3)

    
s1 = Student("Agrim",[99,98,99])
s1.greet()
s1.Avg()"""

#Abstraction and Encapsulation
"""class Account:
    def __init__(self,Balance,Acc):
        self.Balance = Balance
        self.Acc_no  = Acc
        
    def debit(self,Amount):
        self.Balance -=Amount
        print(self.Balance)
        print("Total Balance:",self.get_balance())
        
    def credit(self,Amount):
        self.Balance += Amount
        print(self.Balance)

    def get_balance(self):
        return self.Balance    

acc1 = Account(20000,12345)
print(acc1.Balance)
print(acc1.Acc_no)
acc1.debit(1000)
acc1.credit(2000)"""

#Delete keyword:It is used to delete the object properties or object itself
"""class Student:
    def __init__(self,name,roll):
        self.name = name
        self.roll = roll
        
s1 = Student("Agrim","0034")
print(s1.name)
print(s1.roll)

del s1.name #name deleted
del s1 #object deleted"""

#Private attributes and methods:use double under score before an attribute
#Attribute
"""class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass#private
        
    def reset_pass(self):
        print(self.__acc_pass)#It will run bcs it is in same class
        
acc1 = Account("12345","x9FAW")

print(acc1.acc_no)
#print(acc1.__acc_pass)#It will not run bcz the attribute is private
acc1.reset_pass()"""

#Method
"""class Person:
    __name = "anonymous"
    
    def __hello(self,name):
        print("Hello person!")
        
    def welcome(self):
        self.__hello()
        
p1 = Person()
print(p1.welcome())"""

#Inheritance
"""class Car:
    color = "Black"
    @staticmethod
    def start():
        print("car started...") 
        
    @staticmethod
    def start():
        print("car stopped.")
        
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyotaCar("Fortuner")
car2 = ToyotaCar("Prius")
print(car1.color)
print(car2.start())

#Multi-level inheritance
class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type
    
car1 = Fortuner("Diesel")
car1.start()"""
    
#Multiple inheritance 
"""class A:
    varA = "welcome to class A"
    
class B:
    varB = "welcome to coass B"
    
class C(A,B):
    varC = "welcome to class C"
    
c1 = C()

print(c1.varC)
print(c1.varB)
print(c1.varA)"""

#Super Method
"""class Car:
    def __init__(self,type):
        self.type = type
    
    @staticmethod
    def start():
        print("car started...") 
        
    @staticmethod
    def start():
        print("car stopped.")
        
class ToyotaCar(Car):
    def __init__(self,name,type):
        super().__init__(type)
        self.name = name
        super().start()
        
car1 = ToyotaCar("prius","electric")
print(car1.type)"""

#Class method 
"""class Person:
    name = "anonymous"
    
    def changeName(self,name):
    #This method is alternate of the class method        #Person.name = name
        #self.__class__.name = name
    
    #using class method
    @classmethod
    def changeName(cls,name):
        cls.name = name
        
        
p1 = Person()
p1.changeName("Rahul")
print(p1.name)
print(Person.name)"""

#Property decorator
"""class Student:
    def __init__(self, phy,chem,math):
        self.phy = phy
        self.chem = chem
        self.math = math
        #self.percentage = str((self.phy+self.chem+self.math)/3)+"%"
        
    @property #This will update the percentage 
    def percentage(self):
        return  str((self.phy+self.chem+self.math)/3)+"%"

s1 = Student(98,97,99)       
print(s1.percentage)

s1.phy = 86
print(s1.phy)
print(s1.percentage)#This percentage is not autometically change when the marks also updated,So we will use the PROPERTY decorator"""

#POLYMORPHISM:operator overloadinhg
#IMPLICIT OVERLOADING
"""print(1+2) #3
print(type(1))#already defined class int

print("Agrim " + "Patel") #Concatenate
print(type("apna"))#Already defined class string

print([1,2,3]+[4,5,6]) #Merging of list
print(type([1,2,3]))#Already defined class list"""

#EXPLICIT OPERATOR OVERLOADING
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"+",self.img,"i") 
        
    def __add__(self,num2):
        newReal = self.real + num2.real 
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    def __sub__(self,num2):
        newReal = self.real - num2.real 
        newImg = self.img - num2.img
        return Complex(newReal,newImg)  
        
num1 = Complex(4,5)
num1.showNumber()

num2 = Complex(3,2)
num2.showNumber()

num3 = num1.__add__(num2)
num3.showNumber()

num4 = num1.__sub__(num2)
num4.showNumber()


    