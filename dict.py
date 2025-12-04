#Dictionory:collection of key value parts
a = {
    "Harry" : 98,
    "Shubham":99,
    "Raj":97,
    "list":[1,2,3,4]
}
"""print(a,type(a))
print(a["list"])"""
#some methods of dictionaries
"""print(a.items())
print(a.keys())#left side cotent 
print(a.values())#Right side content
a.update({"Harry" : 100 , "Renuka": 98})"""
print(a)
print(a.get("Harry"))#returns the value of key element amd return NAN if thr key is not present in dictionary
print(a["Harry"])#is returns error if the key is not present in dict.