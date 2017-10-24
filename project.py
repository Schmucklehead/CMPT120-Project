#Jake Tantorski CMPT 120L 9/21/17

global score
score = 0

global name




rocks = ("You stumble upon a rocky surface. The is no life to be seen and water is scarce.")
beach = ("A beach appears. Waves crash against the sandy beach and palm trees sway in the wind.")
cave = ("Between some bushes a cave is visible. You walk inside and see many drawings on the wall and a torch lit in the back.")
forest = ("A thick forest appears with many tall luming trees. Animals are abdunant and you smell pine.")
field = ("Now a lush grassy field is in your sights. The grass is untouched except the small rodents that live in it. Flies buzz around your head in the heat.")
village = ("You can make out what seems to be an old village. A fire is almost out and spears are lying around.")


beenThereRocks = False
beenThereBeach = False
beenThereCave = False
beenThereForest = False
beenThereField = False
beenThereVillage = False

myLoc = beach
print("WELCOME TO ISLAND SURVIVAL!")
name = input(str("Enter your name: "))

title = ("Island Survival is a text based game. Contorls are: East, West, North, South, Help and Quit. On this adventure" ,name,  "will enter into many locations. Hopefully you can make it out alive.")
def intro():
    print(title)
    
intro()

def game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage):

 moves = 0    



 while True:
        if(myLoc == cave):
            endingScene()
            break
        elif(moves == 20):
            print("Too many moves and you got caught in the cold! You lose!")
            break                 
        else:
            
        #Rocks
            if(myLoc == rocks):
                direction = input("Pick a direction: ")
                if(direction.lower() == "south"):
                    moves = moves+1
                    myLoc= beach
                    print(myLoc)
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True
                    

                elif(direction.lower() == "east"):
                    moves = moves+1
                    myLoc = cave
                    print(myLoc)
                    if(beenThereCave == False):
                        score = score + 5
                        beenThereCave = True
                        
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                else:
                    print("It looks like you cant go that way. Try another direction.")
                    

            
            #Beach
            elif(myLoc == beach):
                direction = input("Pick a direction: ")
                if(direction.lower()== "north"):
                    moves = moves+1
                    myLoc= rocks
                    print(myLoc)
                    if(beenThereRocks == False):
                        score = score + 5
                        beenThereRocks = True
                    
                        
                elif(direction.lower() == "south"):
                    moves = moves+1
                    myLoc = village
                    print(myLoc)
                    if(beenThereVillage == False):
                        score = score + 5
                        beenThereVillage = True
                elif(direction.lower() == "east"):
                    moves = moves+1
                    myLoc = forest
                    print(myLoc)
                    if(beenThereForest == False):
                        score = score + 5
                        beenThereForest = True
                    
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = field
                    print(myLoc)
                    if(beenThereField == False):
                        score = score + 5
                        beenThereField = True
                    
                        
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
            elif(myLoc == field):
                direction = input("Pick a direction:")
                if(direction.lower() == "south"):
                    moves = moves+1
                    myLoc = village
                    print(myLoc)
                    if(beenThereVillage== False):
                        score = score + 5
                        beenThereVillage = True
                    
                elif(direction.lower()== "east"):
                    moves = moves+1
                    myLoc = beach
                    print(myLoc)
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True

                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                else:
                    print("It looks like you cant go that way. Try another direction.")
            #Village
            elif(myLoc == village):
                direction = input("Pick a direction: ")
                if(direction.lower() == "north"):
                    moves = moves+1
                    myLoc= beach
                    print(myLoc)
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True
                    
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = field
                    print(myLoc)
                    if(beenThereField == False):
                        score = score + 5
                        beenThereField = True
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                else:
                    print("It looks like you cant go that way. Try another direction.")
            #Forest
            elif(myLoc == forest):
                direction = input("Pick a direction: ")
                if(direction.lower() == "north"):
                    moves = moves+1
                    myLoc = cave
                    print(myLoc)
                    if(beenThereCave == False):
                        score = score + 5
                        beenThereCave = True
                    
                elif(direction.lower() == "south"):
                    moves = moves+1
                    myLoc = village
                    print(myLoc)
                    if(beenThereVillage == False):
                        score = score + 5
                        beenThereVillage = True
                    
                elif(direction.lower() == "west"):
                    moves = moves+1
                    myLoc = beach
                    print(myLoc)
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                     game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
                elif(direction.lower() == "quit"):
                    quit()
                elif(direction.lower() == "points"):
                     print(name + "'s score is: " + str(score))
                else:
                    print("It looks like you cant go that way. Try another direction.")
                    game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)

        
            
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
    
    
                
game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)





    
        






print("Copyright: Jake Tantorski jake.tantorski1@gmail.com ")


