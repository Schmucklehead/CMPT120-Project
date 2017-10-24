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
 
    
    while True:
        if(myLoc == cave):
            break
        else:
            print(myLoc)
        #Rocks
            if(myLoc == rocks):
                direction = input("South or East: ")
                if(direction.lower() == "south"):
                    myLoc= beach
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True
                    

                elif(direction.lower() == "east"):
                    myLoc = cave
                    if(beenThereCave == False):
                        score = score + 5
                        beenThereCave = True
                        
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                else:
                    print("It looks like you cant go that way. Try another direction.")
                    

            
            #Beach
            if(myLoc == beach):
                direction = input("North, East or South: ")
                if(direction.lower()== "north"):
                    myLoc= rocks
                    if(beenThereRocks == False):
                        score = score + 5
                        beenThereRocks = True
                    
                        
                elif(direction.lower() == "south"):
                    myLoc = village
                    if(beenThereVillage == False):
                        score = score + 5
                        beenThereVillage = True
                elif(direction.lower() == "east"):
                    myLoc = forest
                    if(beenThereForest == False):
                        score = score + 5
                        beenThereForest = True
                    
                elif(direction.lower() == "west"):
                    myLoc = field
                    if(beenThereField == False):
                        score = score + 5
                        beenThereField = True
                    
                        
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                else:
                    print("It looks like you cant go that way. Try another direction.")

            #Field
            if(myLoc == field):
                direction = input("East or South: ")
                if(direction.lower() == "south"):
                    myLoc = village
                    if(beenThereVillage== False):
                        score = score + 5
                        beenThereVillage = True
                    
                elif(direction.lower()== "east"):
                    myLoc = beach
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True

                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                else:
                    print("It looks like you cant go that way. Try another direction.")
            #Village
            if(myLoc == village):
                direction = input("North or West: ")
                if(direction.lower() == "north"):
                    myLoc= beach
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True
                    
                elif(direction.lower() == "west"):
                    myLoc = field
                    if(beenThereField == False):
                        score = score + 5
                        beenThereField = True
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                elif(direction.lower() == "quit"):
                    quit()
                else:
                    print("It looks like you cant go that way. Try another direction.")
            #Forest
            if(myLoc == forest):
                direction = input("North, West or South: ")
                if(direction.lower() == "north"):
                    myLoc = cave
                    if(beenThereCave == False):
                        score = score + 5
                        beenThereCave = True
                    
                elif(direction.lower() == "south"):
                    myLoc = village
                    if(beenThereVillage == False):
                        score = score + 5
                        beenThereVillage = True
                    
                elif(direction.lower() == "west"):
                    myLoc = beach
                    if(beenThereBeach == False):
                        score = score + 5
                        beenThereBeach = True
                    
                elif(direction.lower() == "help"):
                     print("Pick one of the given locations.")
                     game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
                elif(direction.lower() == "quit"):
                    quit()
                else:
                    print("It looks like you cant go that way. Try another direction.")
                    game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)

        
            
       
        
                
game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)




def endingScene():
    print(name + "wins. You have succesfully made it to a safe location to spend the night")
endingScene()
    
    
        






print("Copyright: Jake Tantorski jake.tantorski1@gmail.com ")


