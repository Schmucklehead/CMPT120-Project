#Jake Tantorski CMPT 120L 9/21/17


global name
global score
score = 0
global currLoc
global shortLoc
global userAction
global moves
moves = 0
global ending

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

beach = 0
rocks = 1
cave = 2
forest = 3
field = 4
village = 5
hills = 6
river = 7
marsh = 8
waterfall = 9

directions = [ "north", "south", "east", "west", "quit","look","map","search","take","help","points"]
north = 0
south = 1
east = 2
west = 3
quit = 4
look = 5 
map = 6
search = 7
take = 8
help = 9
points = 10

world = [  #N           #S          #E         #W
         [ rocks,       village,     forest,    field  ]#beach
        ,[ None,        beach,       cave,     hills   ]#rocks
        ,[ None,        forest,      None,      rocks  ]#cave
        ,[ cave,        river,       None,      beach  ]#forest
        ,[ hills,       village,     beach,     None   ]#field
        ,[ beach,       marsh,       river,     field  ]#village
        ,[ None,        field,       rocks,     None   ]#hills
        ,[ forest,      waterfall,   None,      village]#river
        ,[ village,     None,        waterfall, None   ]#marsh
        ,[ river,       None,        None,      marsh  ]#waterfall
        ]
    
    
items = ["life vest", None , None,"map", None, "spear", None, None,None,None]

loc = [("A beach appears. Waves crash against the sandy beach and palm trees sway in the wind."),
       ("You stumble upon a rocky surface. The is no life to be seen and water is scarce."),
       ("Between some bushes a cave is visible. You walk inside and see many drawings on the wall and a torch lit in the back."),
       ("A thick forest appears with many tall luming trees. Animals are abdunant and you smell pine."),
       ("Now a lush grassy field is in your sights. The grass is untouched except the small rodents that live in it. Flies buzz around your head in the heat."),
       ("You can make out what seems to be an old village. A fire is almost out and spears are lying around."),
       ("As the sun glares in your eyes you see that the hills in front of you are rolling everywhere. Grass is covering the hills and an eagle flys above"),
       ("Water is rushing past you and you gaze upon a giant river. Swimming through seems to be your only way of crossing"),
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
beenThere = [
              beenThereBeach
             ,beenThereRocks
             ,beenThereCave
             ,beenThereForest
             ,beenThereField
             ,beenThereVillage
             ,beenThereHills
             ,beenThereRiver
             ,beenThereMarsh
             ,beenThereWaterfall
            ]
examThereRocks = False
examThereBeach = False
examThereCave = False
examThereForest = False
examThereField = False
examThereVillage = False
examThereHills = False
examThereRiver = False
examThereMarsh = False
examThereWaterfall = False
examThere = [
              examThereBeach
             ,examThereRocks
             ,examThereCave
             ,examThereForest
             ,examThereField
             ,examThereVillage
             ,examThereHills
             ,examThereRiver
             ,examThereMarsh
             ,examThereWaterfall
            ]

print("WELCOME TO ISLAND SURVIVAL!")
name = input(str("Enter your name: "))

inven = []

def intro():
    print()
    print("Island Survival is a text based game. Controls are: East, West, North, South, Help, Points, Search, Take, Map and Quit. On this adventure" ,name,  "will enter into many locations. Hopefully you can make it out alive.")
    print()
    print("You have awoken on a sandy shore with a seagull staring you right in the face. You rub your eyes and look around. You do not remember anything except your name and a few other basic skills. Unsure of what to do you start looking around.")
    print()
def main():   
    intro()
    game()
    endingScene()
#Game Function
def game():
    global userAction
    global score
    global moves
    global ending
 
    currLoc = beach
    printLoc(currLoc)
    while True:                     
     if currLoc == river and not "life vest" in inven:
         ending = 2
         break
     elif moves == 40:
        ending = 1
        break
     elif currLoc == cave and "spear" in inven:
         ending = 0
         break
     elif score == 50 and "map" in inven:
         ending = 3
         break
     
     else:
        userAction = getNextDirection()
        if userAction == quit:
            break
        elif userAction == look :
            print(loc[currLoc])
            
        elif userAction == map :
            drawMap()

        elif userAction == search:
            searchForItem(currLoc)

        elif userAction == take:
            takeItem(currLoc)

        elif userAction == help:
            print("Commands are: -North-, -South-, -East- , -West-. -Quit- to end the game, -Look- to look around, -Map- to access map, -Search- to search for items, -Take- to take the items after searching, -Points- to show " + name + "'s score.")
            
        elif userAction == points:
            print("Score: " + str(score) + ".")
        
        else:
            currLoc = lookUpLoc(currLoc,userAction)
            printLoc(currLoc)
            moves = moves + 1

def endingScene():
    global ending
    if (ending == 0):
        print(name + " wins. You have succesfully made it to a safe location with a weapon to spend the night")

    elif(ending  == 1):
        print("You took too long and got caught in the cold of the night. You died. GAME OVER!")

    elif(ending == 2):
        print("You did not have something to keep you afloat as tried to cross and you drowned. GAME OVER!")

    elif(ending == 3):
        print("You have been everywhere and you have the map with you. You have seen the island and can survive and navigate!")

    else:
        print("Thanks for playing!")
def getNextDirection():
        choice = input("Command: ").strip().lower()
        try:
            return directions.index(choice)
        except:
            print("Thats not a valid command!")
            return getNextDirection()

        
        
def lookUpLoc(location, directions):
    if world[location][directions] == None:
       print("There is nothing in that direction.")
       return location
    else:
        return world[location][directions]

    

def printLoc(place):
    global score
    if(beenThere[place] == False):
        print(loc[place])
        score = score + 5
        beenThere[place] = True
    else:
        if(userAction == look):
            pass
        else:
            print(shortLoc[place])

            

def searchForItem(place):
    global itemsLoc
    global inven
    global examThere
    global moves
    moves = moves + 1
    examThere[place] = True
    if items[place] != None:
        print("Look an item!")  
    else:
        print("Nothing here.")

def takeItem(place):
    global itemsLoc
    global inven
    global examThere
    global moves
    moves = moves + 1
    if examThere[place] == False: 
        print("You need to search for an item first!")
    else:
        if items[place] == None:
            print("I guess there is nothing here.")
        else:
            inven.append(items[place]) 
            print("Congrats, You found a " + items[place]+ ".")
            items[place] = None 
        
        
        

#Map Of Island
def drawMap():
  if "map" in inven:
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
  else:
       print("You do not have a map with you.")

                       
main()

print("Copyright: Jake Tantorski jake.tantorski1@marist.edu ")


