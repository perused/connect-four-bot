import os
import sys

def greeting():
    valid = False
 
    print("Welcome to the connect four bot! The bot is a command line application that takes in a number from 0-6 to identify what the last move was, where 0 is the first column and 6 is the last column. Would you like to start the game? (y/n)", end = " ")

    while not valid:
        starter = input()
        if "y" in starter and "n" not in starter:
            return True
        
        elif "n" in starter and "y" not in starter:
            return False

        else:
            print("Invalid input, please type y or n to indicate if you would like to start: ", end = "")

def main():
    
    user_begins = greeting()

if __name__=="__main__":
    main()
