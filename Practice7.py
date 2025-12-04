#Problem1
"""class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def Area(self):
        return 3.14*self.radius**2
    
    def Perimeter(self):
        return 2*3.14*self.radius
    
c1 = Circle(3)
print(c1.Area())
print(c1.Perimeter())"""

#Problem2
"""class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary
        
    def showDetails(self):
        print("Role:",self.role)
        print("Dept.:",self.department)
        print("Salary:",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","80,000")
        
    def showDetails(self):
        print("Name:",self.name)
        print("Age:",self.age)
        super().showDetails()
        
e1 = Engineer("Agrim","26")
e1.showDetails()"""

#Problem3
"""class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    def __gt__(self,odr2):
        return self.price > odr2.price
    
odr1 = Order("chips",20)
odr2 = Order("Tea",15)

print(odr1 > odr2)"""   #True 

#Problem4
"""class TwoDVector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")
        
class ThreeDVector(TwoDVector):
    def __init__(self,i,j,k):
        super().__init__(i,j)
        self.k = k
        
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
        
        
v1 = TwoDVector(4,6)
v2 = ThreeDVector(9,8,7)
v1.show()
v2.show()"""

#Problem5
"""class Animals:
    pass

class Pets(Animals):
    pass
    
class Dog(Pets):
    @staticmethod
    def bark():
        print("Dog is barking....")
        
d = Dog()
d.bark()"""

#Problem6
"""class Employee:
    salary = 243
    increment = 20
    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary*(self.increment/100))
    
    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1)*100

e = Employee()
print("The salary after increment is:",e.salaryAfterIncrement)
print("The incrment in salary is:",e.increment)"""

#Problem7
"""class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k 
        
    def showVector(self):
        print(self.i,"i +",self.j,"j +",self.k,"k")
        
    def __add__(self,v2):
        return Vector(self.i+v2.i,self.j+v2.j,self.k+v2.k)    
    
    def __mul__(self,v2):
        return Vector(self.i*v2.i,self.j*v2.j,self.k*v2.k) 

v1 = Vector(3,4,5)
v2 = Vector(1,6,3)
v1.showVector()
v2.showVector()
v3 = v1.__add__(v2)
v3.showVector()
v4 = v1.__mul__(v2)
v4.showVector()"""

#Problem8 
"""class Vector1:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def showVector(self):
        print(f"{self.i}i + {self.j}j + {self.k}k")
        
v1 = Vector1(7,8,10) 
v1.showVector()"""

#Problem9
class Vector2:
    def __init__(self,l):
        self.l = l
        
    def __len__(self):
        return len(self.l)
    
v = Vector2([1,2,3])
print("The length of the given vector is:",len(v))
        
    
    


  
    

        
    
        