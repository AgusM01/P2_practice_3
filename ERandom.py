#Exercises using random function
import random

#1
#Simulate a 7 faces dice and it won't stop until the dice gives a 7
#dice_Simulation: None --> None
def dice_Simulation():
    dice = 0
    while dice != 7:
        dice = random.randrange(8)
        print (dice)

#2
#Throw two dices n times and count everytime the dice were equal
#two_Dices: None --> Int
#receive a number n to indicates how many roll will be
#gives an int indicating how many times the dice were equal
def two_Dices():
    dice1 = 0
    dice2 = 0
    n = int(input("Enter the number of times to roll the dice "))
    t = 0
    while n != 0:
        dice1 = random.randrange(7)
        dice2 = random.randrange(7)
        if dice1 == dice2:
            t = t + 1
        
        n = n - 1
    print ("The dice were equal: ", t, " times")
    #return t 
    # If you want to include this function in a bigger
    # program, uncomment the return line and erase the print

#two_Dices() 
        

#3
#Throw a dice N times
#If it was 6, add 4 pesos, if 3, add 1 dollar
#if 2, 4 or 5, rest 2 pesos
#dice_Game: None --> None  
def dice_Game():
    dice0 = 0
    p = 0
    d = 0
    h = n = int(input("Enter the number of times to roll the dice "))

    while h != 0:
        dice0 = random.randrange(7)
        if dice0 == 6:
            p = p + 4
        elif dice0 == 3:
            d = d + 1
        elif dice0 == 2 or dice0 == 4 or dice0 == 5:
            p = p - 2
        
        h = h - 1
    print ("You win: ", p, "pesos, and: ", d, "dollars." )

#dice_Game()

