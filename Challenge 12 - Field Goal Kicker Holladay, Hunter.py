import random

#Goal takes the probaility given to it and uses random to tell us if the field goal was made or not and give 3 points for each made field goal
def goal (prob):
    RanNum = random.randint(1, 100)
    if RanNum >=prob:
        points = 0
        return points
    else:
        points = 3
        return points
###################################################################################################################################################################################################################################    
def chances():
    #Setting the itnital yards for kicks to 10 and starting a list for points
    yards = 10 
    Point = []
#Using a for loop to run the chunk of code for 5 kickes
    for i in range (5):
#Asking for a number for prob and waiting for the number The While True will break once a number is inserted
        while True:
            try:
                prob = int(input("What is the the probability of you making a "+str(yards)+" yard field goal: "))
                break
            #If they have a Value Error where they dont enter a number it asked them to try again
            except ValueError:
                print("Invalid input! Please enter a valid number.")
#Once prob is given it is ran through Goal and the points are append into Points
        points = goal(prob)
        Point.append(points)
        yards = yards + 10
#Take the sum of all the points in the list and uses that to assign if they win or lost
    points = sum(Point)
    if points == 15:
       a = print("You scored "+str(points)+" points\n Great Job! You got a perfect score!")
       return(a)
    elif points >= 9:
        a = print("You scored "+str(points)+" points\nGood job you have won")
        return(a)
    else:
        a = print("You scored "+str(points)+" points\nSo sorry but you lost")
        return(a)
###################################################################################################################################################################################################################################    
def restart(WinLose):
    #Print if player win/lost
    WinLose
    #Ask if they would like to play agian
    while True:
        Use = str(input("Would you like to restart the program (Yes/No): "))
        if Use.lower() == "yes":
            mid();
            break
        elif Use.lower() == "no":
            print("Thank you for your time have a great day")
            input("Press <ENTER> to quit")
            exit()
        else:
             print("Your Input is not supported")

###################################################################################################################################################################################################################################    
def mid():
    #If they want to play agian they are sent here as a midground to connect the chances and restart
     WinLose = chances();
     restart(WinLose);
###################################################################################################################################################################################################################################    

def Intro():
    print("The purpose of this code is to play a field goal game where you\ngive the probability of you making five field goals the goal\n is to score 9 points to win but as always you want a perfect game.")
#Asking the User if they want to play if they do they get to play if they dont the app closes
    while True:
        Use = str(input("Would you like to play a game (Yes/No): "))

        if Use.lower() == "yes":
            #Sends the user to chances where the game will end
            WinLose = chances();
            break
    
        elif Use.lower() == "no":
            print("Thank you for your time have a great day")
            input("Press <ENTER> to quit")
            exit()
        else:
            print("Your Input is not supported")

    restart(WinLose);

Intro();
