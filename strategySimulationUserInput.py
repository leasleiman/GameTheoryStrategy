#author: Lea
#"""

#Name: Lea Sleiman
#FileName: gameTheory
#Description: This program simulates a game theory situation specifically a prisonner's dilmma game
#             the point of the game is to test the tit for tat strategy!
#             There are 2 strategies: defect or cooperate 
#             There are 2 players: computer and user
#             The game will be played for 5 rounds    



#Import Random library 

import random 

#---------------------------------Function Definition:-----------------------------------------------

#This function has no inputs. it prints a 2d array in the form of a matrix
#this matrix represents the payoff matrix used in my game simulation 

def displayMatrix():
    print('You have 2 strategies: you can cooperate or defect. ')
    print('')
    payoffMatrix=[['   C       D'],['C  3,3    0,5'],['D  5,0    1,1']]
    print('This is your payoff Matrix: ')
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
          for row in payoffMatrix]))
    print('')
    



#Game points is a function that takes two inputs:
#                               -The player's Strategy
#                               -The computer's strategy
#The function will compare both strategies and accordingly print the outcome


def gameResults (playerChoice, computerChoice):
    
    #In this case both players go for the same strategy
    if computerChoice == playerChoice:
        
        #If both players go for c it means that they both cooperated
        if playerChoice == 'c':
            print ('You both cooperated!')
        
        #If they don't go for c it means both players defected
        else:
            print ('You both defected' )
        
    #In this case both players go for a different strategy
    else:
        
        #the player went for c which means the computer deffected 
        if playerChoice == 'c':
            print('Your opponent defected :( ')
            
        #In thi case the computer cooperated but the user decided to defect
        else:
            print('Your opponent cooperated ;) ')

#This will set the computer's strategy to defector no matter what the user's stretegy is 
def defector():
    computerChoice= 'd'
    return computerChoice 

#This will set the computer's strategy to cooperator no matter what the user does
def cooperator():
    computerChoice='c'
    return computerChoice
        
#------------------------------------------MAIN FUNCTION:-----------------------------------------
           
def Main():
    
    #This will first diplay the payoff matrix and introduce the user to the game situation 
    displayMatrix()   
    
    #The user will choose a random number between 1, 2, 3 and 4
    print('Randomly pick a number between 1 and 4 the computer will choose its strategy accordingly.')
    computerUserChoice=int(input('What number do you choose: '))
    print('The computer strategy is set. The game starts now!')
    print('')
    print('What Strategy will you choose? ')


    #if the user's choice is 1, the computer's strategy will be set as defector no matter what for the 5 rounds
    
    if computerUserChoice == 1:
        
        for i in range(5):
        
            #Setting the computers choice as defector
            computerStrategy= defector()
            
            #Asking for a strategy
            playerStrategy=input('C= Cooperate and D= Defect: ')
            
            # #Game results is called to see who "won" in every round
            gameResults(playerStrategy, computerStrategy) 
            print('')
    

    #if the user's choice is 2, the computer's strategy will be set as cooperator no matter what for the 5 rounds
    
    elif computerUserChoice == 2:
        
        for i in range(5):
        
            #Setting the computers choice as cooperator
            computerStrategy= cooperator()
            
            #Asking for a new user strategy
            playerStrategy=input('C= Cooperate and D= Defect: ')
            
            # #Game results is called to see who "won" in every round
            gameResults(playerStrategy, computerStrategy) 
            print('')
          
    
    #In the user's choice is 3 the computer will play the tit for tat strategies    
    
    elif computerUserChoice == 3:
        
        playerStrategy= input('C= Cooperate and D= Defect: ')
        
        #There are 2 strategies the players can choose from: they can choose to cooperate (c) or to defect(d)
        strategy=['c','d']
        
        #In this first simulation the computer will choose randomly between defecting and cooperating
        computerStrategy = random.choice(strategy)
        
        #Game results is called to see who "won" this first round
        gameResults(playerStrategy, computerStrategy)        
        print('')
        
        #The game will then enter a for loop. The point of this for loop is to play the game repeatedly (overall 5 times)
        #The difference this time is that the computer not play a random strategy
        #the computer will mimic the user's previous choice 
        #meaning that the computer strategy depends on what the user plays first 
        
        for i in range(4):
            
            #Setting the computers choice as the users previous/old choice 
            computerStrategy=playerStrategy
            
            #Asking for a new user strategy
            playerStrategy=input('C= Cooperate and D= Defect: ')
            
            # #Game results is called to see who "won" in every round
            gameResults(playerStrategy, computerStrategy) 
            print('')

    #If the computer's choice is 4 the computer will randomly choose between tit for tat, defector, and cooperator
    else:
        
        #The computer will randomly choose between the 3 strategies available 
        choiceList =[1,2,3]
        computerChoice = random.choice(choiceList)
        
        if computerChoice == 1:
            
            for i in range(5):
            
                #Setting the computers choice as defector
                computerStrategy= defector()
                
                #Asking for a strategy
                playerStrategy=input('C= Cooperate and D= Defect: ')
                
                # #Game results is called to see who "won" in every round
                gameResults(playerStrategy, computerStrategy) 
                print('')
        
        elif computerChoice == 2:
            
            for i in range(5):
            
                #Setting the computers choice as cooperator
                computerStrategy= cooperator()
                
                #Asking for a strategy
                playerStrategy=input('C= Cooperate and D= Defect: ')
                
                # #Game results is called to see who "won" in every round
                gameResults(playerStrategy, computerStrategy) 
                print('')
                
        elif computerChoice == 3:
            
            playerStrategy= input('C= Cooperate and D= Defect: ')
            
            #There are 2 strategies the players can choose from: they can choose to cooperate (c) or to defect(d)
            strategy=['c','d']
            
            #In this first simulation the computer will choose randomly between defecting and cooperating
            computerStrategy = random.choice(strategy)
            
            #Game results is called to see who "won" this first round
            gameResults(playerStrategy, computerStrategy)        
            print('')
            
            #The game will then enter a for loop. The point of this for loop is to play the game repeatedly (overall 5 times)
            #The difference this time is that the computer not play a random strategy
            #the computer will mimic the user's previous choice 
            #meaning that the computer strategy depends on what the user plays first 
            
            for i in range(4):
                
                #Setting the computers choice as the users previous/old choice 
                computerStrategy=playerStrategy
                
                #Asking for a new user strategy
                playerStrategy=input('C= Cooperate and D= Defect: ')
                
                # #Game results is called to see who "won" in every round
                gameResults(playerStrategy, computerStrategy) 
                print('')

    k=input('Game is over! Press close to exit.' )
    
#---------------------------- PROGRAM: Calling our main function:---------------------------------------------   
Main()
