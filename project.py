#Jake Tantorski CMPT 120L 9/21/17


global name
global score
global myLoc
global shortLoc

#0 = beach
#1 = rocks
#2 = cave
#3 = forest
#4 = field
#5 = village
#6 = hills
#7 = river
#8 = marsh
#9 = waterfall


loc = [("A beach appears. Waves crash against the sandy beach and palm trees sway in the wind."),
       ("You stumble upon a rocky surface. The is no life to be seen and water is scarce."),
       ("Between some bushes a cave is visible. You walk inside and see many drawings on the wall and a torch lit in the back."),
       ("A thick forest appears with many tall luming trees. Animals are abdunant and you smell pine."),
       ("Now a lush grassy field is in your sights. The grass is untouched except the small rodents that live in it. Flies buzz around your head in the heat."),
       ("You can make out what seems to be an old village. A fire is almost out and spears are lying around."),
       ("As the sun glares in your eyes you see that the hills in front of you are rolling everywhere. Grass is covering the hills and an eagle flys above"),
       ("Water is rushing past you and you gaze upon a giant river. You see a bridge and it seems to be your only way of crossing"),
       ("You stumble upon a marsh and see ducks flying around and a beaver creating a dam"),
       ("A beautiful waterfall comes into sight and the water sparys your face.  You stare into the beauty that is water falling from a cliff and listen to it crash onto the rocks below")]

shortLoc = [("You are at the beach.")
        ,("You are at the rocks.")
        ,("You are at the cave.")
        ,("You are at the forest.")
        ,("You are at the field.")
        ,("You are at the village.")
        ,("You are at the hills.")
        ,("You are at the river.")
        ,("You are at the marsh.")
        ,("You are at the waterfall.")]

beenThereRocks = False
beenThereBeach = False
beenThereCave = False
beenThereForest = False
beenThereField = False
beenThereVillage = False
beenThereHills = False
beenThereRiver = False
beenThereMarsh = False
beenThereWaterfall = False
beenThere = [beenThereBeach, beenThereRocks, beenThereCave, beenThereForest, beenThereField, beenThereVillage, beenThereHills,beenThereRiver,beenThereMarsh,beenThereWaterfall]
myLoc = loc[0]

print("WELCOME TO ISLAND SURVIVAL!")
name = input(str("Enter your name: "))


def intro():
    print()
    print("Island Survival is a text based game. Contorls are: East, West, North, South, Help, Points, Map and Quit. On this adventure" ,name,  "will enter into many locations. Hopefully you can make it out alive.")
    print()
    print("You have awoken on a sandy shore with a seagull staring you right in the face. It is holding a piece of paper that you quickly grab. You open it and see a map drawn of what you guess is the island. You rub your eyes and look around. You do not remember anything except your name and a few other basic skills. Unsure of what to do you start looking around.")
    print()
    
intro()
#Game Function
def game():




 global score 
 global moves
 global myLoc

 moves = 0
 score  = 0



 while True:
        if(myLoc == loc[2]):
            endingScene()
            break
        elif(moves == 15):
            print("You took too long and you got caught in the cold! You lose!")
            break                 
        else:
            
        #Rocks
            if(myLoc == loc[1]):
                direction = input("Enter a command: ")
                if(direction.lower() == "south"):
 
                    moveTo(0)
                elif(direction.lower() == "east"):

                    moveTo(2)
                elif(direction.lower() == "west"):

                    moveTo(6)
                elif(direction.lower() == "help"):
                     print("Contorls are: East, West, North, South, Help, Points, Map and Quit.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                else:
                    print("It looks like that is not a command. Try another command.")
                    

            


            #Beach
            elif(myLoc == loc[0]):
                direction = input("Enter a command: ")
                if(direction.lower()== "north"):

                    moveTo(1)
                elif(direction.lower() == "south"):

                    moveTo(5)
                elif(direction.lower() == "east"):

                    moveTo(3)
                elif(direction.lower() == "west"):

                    moveTo(4)
                elif(direction.lower() == "help"):
                     print("Contorls are: East, West, North, South, Help, Points, Map and Quit.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                elif(direction.lower() == "look"):
                    print(myLoc)
                else:
                    print("It looks like that is not a command. Try another command.")




            #Field
            elif(myLoc == loc[4]):
                direction = input("Enter a command:")
                if(direction.lower() == "south"):

                    moveTo(5)
                elif(direction.lower()== "east"):

                    moveTo(0)
                elif(direction.lower() == "north"):

                    moveTo(6)
                elif(direction.lower() == "help"):
                     print("Contorls are: East, West, North, South, Help, Points, Map and Quit.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                elif(direction.lower() == "look"):
                    print(myLoc)
                else:
                    print("It looks like that is not a command. Try another command.")






            #Village
            elif(myLoc == loc[5]):
                direction = input("Enter a command: ")
                if(direction.lower() == "north"):

                    moveTo(0)
                elif(direction.lower() == "west"):

                    moveTo(4)
                elif(direction.lower() == "east"):

                    moveTo(7)
                elif(direction.lower() == "help"):
                     print("Contorls are: East, West, North, South, Help, Points, Map and Quit.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                elif(direction.lower() == "look"):
                    print(myLoc)
                else:
                    print("It looks like that is not a command. Try another command.")




            #Forest
            elif(myLoc == loc[3]):
                direction = input("Enter a command: ")
                if(direction.lower() == "north"):

                    moveTo(2)
                elif(direction.lower() == "south"):

                    moveTo(7)
                elif(direction.lower() == "west"):

                    moveTo(0)
                elif(direction.lower() == "help"):
                     print("Contorls are: East, West, North, South, Help, Points, Map and Quit.")
                     game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                elif(direction.lower() == "look"):
                    print(myLoc)
                else:
                    print("It looks like that is not a command. Try another command.")





            #Hills
            elif(myLoc == loc[6]):
                direction = input("Enter a command: ")
                if(direction.lower() == "south"):

                    moveTo(4)
                elif(direction.lower() == "east"):

                    moveTo(1)
                elif(direction.lower() == "help"):
                     print("Contorls are: East, West, North, South, Help, Points, Map and Quit.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                elif(direction.lower() == "look"):
                    print(myLoc)
                else:
                    print("It looks like that is not a command. Try another command.")







            #river
            elif(myLoc == loc[7]):
                direction = input("Enter a command: ")
                if(direction.lower() == "north"):
            
                    moveTo(3)
                elif(direction.lower() == "west"):
                     
                    moveTo(5)
                elif(direction.lower() == "help"):
                     print("Contorls are: East, West, North, South, Help, Points, Map and Quit.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                elif(direction.lower() == "map"):
                    drawMap()
                elif(direction.lower() == "look"):
                    print(myLoc)
                else:
                    print("It looks like that is not a command. Try another command.")


#End Scene           
def endingScene():
    print(name + " wins. You have succesfully made it to a safe location to spend the night")
#Map Of Island
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
    print("              |            | ")
    print("              |            | ")
    print("              |            | ")
    print("            Marsh-----Waterfall")
    
def moveTo(i):
        global score
        global moves
        global myLoc
        global shortLoc
        moves = moves+1
        myLoc = loc[i]
        short = shortLoc[i]
        
        if(beenThere[i] == False):
            score = score + 5
            beenThere[i] = True
            print(myLoc)
        else:
            print(short)
                
        
            


 
                
game()

print("Copyright: Jake Tantorski jake.tantorski1@marist.edu ")


