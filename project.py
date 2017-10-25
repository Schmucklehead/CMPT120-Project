#Jake Tantorski CMPT 120L 9/21/17


global name
global score
global myLoc


#0 = beach
#1 = rocks
#2 = cave
#3 = forest
#4 = field
#5 = village
#6 = hills
#7 = river


loc = [("A beach appears. Waves crash against the sandy beach and palm trees sway in the wind."),("You stumble upon a rocky surface. The is no life to be seen and water is scarce."),("Between some bushes a cave is visible. You walk inside and see many drawings on the wall and a torch lit in the back."),("A thick forest appears with many tall luming trees. Animals are abdunant and you smell pine."),("Now a lush grassy field is in your sights. The grass is untouched except the small rodents that live in it. Flies buzz around your head in the heat."),("You can make out what seems to be an old village. A fire is almost out and spears are lying around."),("As the sun glares in your eyes you see that the hills in front of you are rolling everywhere. Grass is covering the hills and an eagle flys above"),("Water is rushing past you and you gaze upon a giant river. You see a bridge and it seems to be your only way of crossing")]


beenThereRocks = False
beenThereBeach = False
beenThereCave = False
beenThereForest = False
beenThereField = False
beenThereVillage = False
beenThereHills = False
beenThereRiver = False
beenThere = [beenThereBeach, beenThereRocks, beenThereCave, beenThereForest, beenThereField, beenThereVillage, beenThereHills,beenThereRiver]
myLoc = loc[0]

print("WELCOME TO ISLAND SURVIVAL!")
name = input(str("Enter your name: "))

title = ("Island Survival is a text based game. Contorls are: East, West, North, South, Help, Points, Map and Quit. On this adventure" ,name,  "will enter into many locations. Hopefully you can make it out alive.")
def intro():
    
    print(title)
    
    
intro()

def game(myLoc):
 


 moves = 0
 score  = 0



 while True:
        if(myLoc == loc[2]):
            endingScene()
            break
        elif(moves == 20):
            print("Too many moves and you got caught in the cold! You lose!")
            break                 
        else:
            
        #Rocks
            if(myLoc == loc[1]):
                direction = input("Pick a direction: ")
                if(direction.lower() == "south"):
                    moves = moves+1
                    myLoc= loc[0]
                    moveTo()
                    

                elif(direction.lower() == "east"):
                    moves = moves+1
                    myLoc = loc[2]
                    moveTo()
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = loc[6]
                    moveTo()
                        
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like you cant go that way. Try another direction.")
                    

            


            #Beach
            elif(myLoc == loc[0]):
                direction = input("Pick a direction for start: ")
                if(direction.lower()== "north"):
                    moves = moves+1
                    myLoc = loc[1]
                    moveTo()
 
                    
                        
                elif(direction.lower() == "south"):
                    moves = moves+1
                    myLoc = loc[5]
                    moveTo()
                elif(direction.lower() == "east"):
                    moves = moves+1
                    myLoc = loc[3]
                    moveTo()
                    
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = loc[4]
                    moveTo()
                    
                        
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like you cant go that way. Try another direction.")




            #Field
            elif(myLoc == loc[4]):
                direction = input("Pick a direction:")
                if(direction.lower() == "south"):
                    moves = moves+1
                    myLoc = loc[5]
                    moveTo()
                    
                elif(direction.lower()== "east"):
                    moves = moves+1
                    myLoc = loc[0]
                    
                    moveTo()

                elif(direction.lower() == "north"):
                    moves = moves+1
                    myLoc = loc[6]
                    moveTo()

                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like you cant go that way. Try another direction.")






            #Village
            elif(myLoc == loc[5]):
                direction = input("Pick a direction: ")
                if(direction.lower() == "north"):
                    moves = moves+1
                    myLoc= loc[0]
                    moveTo()
                    
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = loc[4]
                    moveTo()
                    
                elif(direction.lower() == "east"):
                    moves = moves+1
                    myLoc = loc[7]
                    moveTo()
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like you cant go that way. Try another direction.")




            #Forest
            elif(myLoc == loc[3]):
                direction = input("Pick a direction: ")
                if(direction.lower() == "north"):
                    moves = moves+1
                    myLoc = loc[2]
                    moveTo()
                    
                elif(direction.lower() == "south"):
                    moves = moves+1
                    myLoc = loc[7]
                    moveTo()
                    
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = loc[0]
                    print(myLoc)
                    moveTo()
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                     game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like you cant go that way. Try another direction.")





            #Hills
            elif(myLoc == loc[6]):
                direction = input("Pick a direction: ")
                if(direction.lower() == "south"):
                    moves = moves+1
                    myLoc = loc[4]
                    moveTo()
                    
                elif(direction.lower() == "east"):
                    moves = moves+1
                    myLoc = rocks
                    moveTo()
               
                    
                        
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like you cant go that way. Try another direction.")







            #river
            elif(myLoc == loc[7]):
                direction = input("Pick a direction: ")
                
                        
                if(direction.lower() == "north"):
                    moves = moves+1
                    myLoc = loc[3]
                    moveTo()
                
                    
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = loc[5]
                    moveTo()
                    
                        
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like you cant go that way. Try another direction.")


            
def endingScene():
    print(name + " wins. You have succesfully made it to a safe location to spend the night")

def drawMap():
    print("Hills------ Rocks--------Cave")
    print("  |           |            | ")
    print("  |           |            | ")
    print("  |           |            | ")
    print("Field------ Beach--------Forest")
    print("     \        |            | ")
    print("      \       |            | ")
    print("       \      |            | ")
    print("        \---Village-----River")
    
def moveTo():
        global score
        
        if(myLoc== loc[1]):
            print(loc[1])
            if(beenThere[1] == False):
                score = score + 5
                beenThere[1] = True

                
        elif(myLoc== loc[0]):
            print(loc[0])
            if(beenThere[0] == False):
                score = score + 5
                beenThere[0] = True

                
        elif(myLoc== loc[2]):
            print(loc[2])
            if(beenThere[2]== False):
                score = score + 5
                beenThere[2] = True

                
        elif(myLoc== loc[3]):
            print(loc[3])
            if(beenThere[3] == False):
                score = score + 5
                beenThere[3] = True

                
        elif(myLoc== loc[4]):
            print(loc[4])
            if(beenThere[4]== False):
                score = score + 5
                beenThere[4] = True

                
        elif(myLoc== loc[5]):
            print(loc[5])
            if(beenThere[5] == False):
                score = score + 5
                beenThere[5] = True

                
        elif(myLoc==loc[6]):
            print(loc[6])
            if(beenThere[6] == False):
                score = score + 5
                beenThere[6] = True

                
        elif(myLoc == loc[7]):
            print(loc[7])
            if(beenThere[7] == False):
                score = score + 5
                beenThere[7] = True
                
game(myLoc)





    
        






print("Copyright: Jake Tantorski jake.tantorski1@gmail.com ")


