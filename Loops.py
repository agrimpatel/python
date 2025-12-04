#FOR loop
for i in range(1,51):
    print(i)
    
#WHILE loop
i = 0
while(i<51):
    print(i)
    i=i+1
    
#FOR loop with else
li = [1,2,3,4]
for i in li:
    print(i)
else:
    print("Done")    

#Break statement 
for i in range(100):
    if(i==24):
        break
    print(i)
    
    
#Continue statement
for i in range(50):
    if(i==20):
        continue
    print(i)
    
#Pass statement
for i in range(50):
    pass
while(i<100):
    print(i)
    i +=1