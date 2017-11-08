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

directions = [ "north", "south", "east", "west", "quit" ]
north = 0
south = 1
east = 2
west = 3
quit = 4


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


print("WELCOME TO ISLAND SURVIVAL!")
name = input(str("Enter your name: "))

inven = []

def intro():
    print()
    print("Island Survival is a text based game. Contorls are: East, West, North, South, Help, Points, Map and Quit. On this adventure" ,name,  "will enter into many locations. Hopefully you can make it out alive.")
    print()
    print("You have awoken on a sandy shore with a seagull staring you right in the face. It is holding a piece of paper that you quickly grab. You open it and see a map drawn of what you guess is the island. You rub your eyes and look around. You do not remember anything except your name and a few other basic skills. Unsure of what to do you start looking around.")
    print()
def main():   
    intro()
    game()
    ending()
#Game Function
def game():

 
    currLoc = beach
     
    '''
        if(myLoc == loc[2]):
            endingScene()
            break
        elif(moves == 15):
            print("You took too long and you got caught in the cold! You lose!")
            break
            '''
    while True:
        printLoc(currLoc)
        userAction = getNextDirection()
        if userAction == quit: break
        currLoc = lookUpLoc(currLoc,userAction)

def getNextDirection():
        choice = input("Command: ").strip().lower()
        try:
            return directions.index(choice)
        except:
            print("Thats not a valid command!")
            return getNextDirection()
        
def lookUpLoc(location, directions):
        return world[location][directions]

def printLoc(place):
    if(beenThere[place] == False):
        print(loc[place])
        beenThere[place] = True
    else:
        print(shortLoc[place])
        
        
        
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
"""   
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
            """

        


                
        
            


 
                
main()

print("Copyright: Jake Tantorski jake.tantorski1@marist.edu ")


