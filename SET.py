d = {} #Empty dictionary
e = set()#Empty set created
s = {1,3,4,5,5,5,5,6,7,8,78,"Agrim"}
s2 = {7,5,4,6,7,78,"Agrim"}
print(s)
#SET methods
s.add(34)
print(s,type(s))
s.remove(5)
print(s)
#UNION AND INTERSECTION
print(s.union(s2))
print(s.intersection(s2))

