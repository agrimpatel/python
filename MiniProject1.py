#SNAKE,WATER,GUN GAME
import random
'''
1 for snake
2 for water
3 for gun
'''

computer = random.choice([1,2,3])
youstr = input("Enter your choice:")
youDict = {"s": 1,"w": 2,"g":3}
reverseDict = {1:"Snake",2:"Water",3:"Gun"}
you = youDict[youstr]

print(f"You chose: {reverseDict[you]}\nComputer chose: {reverseDict[computer]}")

if(computer == you):
    print("Draw!!")
else:
    if(computer == 2 and you == 1): #1
        print("YOU WIN!!")
    elif(computer == 2 and you == 3): #-1
        print("YOU LOSE!")
    elif(computer == 1 and you == 2): #-1
        print("YOU LOSE!")
    elif(computer == 1 and you == 3): #-2
        print("YOU WIN!!")
    elif(computer == 3 and you == 1): #2
        print("YOU LOSE!")
    elif(computer == 3 and you == 2): #1
        print("YOU LOSE!!")
    else:
        print("Sorry,something went wrong!!")

#Alternate logic for the above program
"""if((computer - you) == -1 or (computer - you) == 2 or (computer - you) == 1):
    print("You lose!")
else:
    print("You win!!")"""
    
    
