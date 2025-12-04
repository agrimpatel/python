def myFunct():#This fuction is called from AdvancePython
    print("Hello World!!")
    
myFunct()
print(__name__)
    

if __name__ == "__main__":
    #If this code is directly executed by running the file its present in 
    print("We are directly running this code")
    myFunct()
    print(__name__)
    
   