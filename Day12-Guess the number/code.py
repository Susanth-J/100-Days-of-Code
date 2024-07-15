import random
from art import logo
# Getting a number between 1 to 50
easy_level=10
hard_level=5

def play(b,number,turns):
        if b==number:
            print("Your guess is correct!!!")
        elif b<number:
            print(f"Your guess {b} is too low!")
            return turns-1
        elif b>number:
            print(f"Your guess {b} is too high!")
            return turns-1

def dificulty(a):
    if a=="easy":
        return easy_level
    elif a=="hard":
        return hard_level
    

def again():
    number=random.randint(1,51) 
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 50: ")
    print(f"Psst, The number is {number}")
    a=input("Choose a Difficulty. Typer 'easy' or 'hard': ").lower() 
    turns=dificulty(a) 
    b=0
    while b != number:
        print(f"You have {turns} left")
        b=int(input("Enter your guess: "))
        turns=play(b,number,turns)
        if turns==0:
          print("You run out of turns!")
          return
        elif b!=number:
          print("Go agin")

again()

    


    

    
            
    
 
    
