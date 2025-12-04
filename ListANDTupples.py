#LIST
"""Friends = ["sarthak","krishna","kushal","saawan",35.6,45,"ajinkya"]
print(Friends)
Friends.append("Alice")
print(Friends)"""
#creating a list of numbers and performing the operations to the list
li = [35,34,56,76,65,45,43,45]
#li.reverse()
#li.sort()
#li.insert(2,76) #insert 76 at the index 2
print(li.pop(3))#It removes the element present at the index 3 
print(li)
#In list w(e can modify the value at any index but in string can't be modified
#TUPLES:immutable data type,means it can't be modified
a = (1,34,45,342,342,False,"Rohan","Agrim")
print(a)
print(type(a))
#Methods in tuple
frequency=a.count(342)
print(frequency)
#using (+) we can concatenate the two/more tuples
print(len(a))

 

 
