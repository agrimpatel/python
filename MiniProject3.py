#THE ROBO SPEAKER
import os
if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. Created by Agrim")
    while True:
        x = input("Enter what you want me to speak:")
        command = f"say {x}"
        os.system(command)#It is used to run the commands prompted by user