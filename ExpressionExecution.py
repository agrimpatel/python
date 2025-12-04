#String and numeric ,String and string 
A,B,C = 2,3,"2"
Txt = "#"
print(2*Txt*3)
print((Txt+C)*2)

#Arithmetic expression with integer and float will result in float,eg:
A,B,C,D = 10,-4.5,1.5,3
print(A*B)
print(A/B)
print(type(A*B))
print(type(A/B))

#Integer division(a//b) with float and int will give int displayes as float,eg:
#Result of (a//b) is same as floor(a/b)
print(A//B,A/B)

#Remainder is negative when denominator is negative otherwise always positive
print(A%B)