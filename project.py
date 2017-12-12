#Jake Tantorski CMPT 120L 12/4/17

from player import *
from gameLocale import *



global userAction
global ending


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
dam = 10
pond = 11

directions = [ "north", "south", "east", "west", "quit","look","map","search","take","help","points","drop","use","inventory", "pray"]
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
drop = 11
use = 12
inventory =13
pray = 14

world = [  #N           #S          #E         #W
         [ rocks,       village,     forest,    field  ]#beach
        ,[ None,        beach,       cave,     hills   ]#rocks
        ,[ None,        forest,      None,      rocks  ]#cave
        ,[ cave,        river,       None,      beach  ]#forest
        ,[ hills,       village,     beach,     None   ]#field
        ,[ beach,       marsh,       river,     field  ]#village
        ,[ None,        field,       rocks,     None   ]#hills
        ,[ forest,      waterfall,   None,      village]#river
        ,[ village,     dam,         waterfall, None   ]#marsh
        ,[ river,       pond,        None,      marsh  ]#waterfall
        ,[ marsh,       None,        pond,      None   ]#dam
        ,[ waterfall,   None,        None,      dam    ]#pond
        ]
    




#The Player Class
userPlayer = Player(0,0,[],"name", beach)
#BEACH
locales = [  GameLocale( "beach", "A beach appears. Waves crash against the sandy beach and"
                           " palm trees sway in the wind.", "You are at the beach.",  False,  False, "lifevest")
#ROCKS
,GameLocale("rocks", "You stumble upon a rocky surface. The is no life"
                           " to be seen and water is scarce.", "You are at the rocks.", False,  False, None)
#CAVE                          
,GameLocale("cave", "Between some bushes a cave is visible. You walk inside and see many "
                          "drawings on the wall and a torch lit in the back.", "You are at the cave.",  False,  False, None)
#FOREST
,GameLocale("forest", "A thick forest appears with many tall luming trees. "
                            "Animals are abdunant and you smell pine.", "You are at the forest.",  False,  False, "wood")
#FIELD
,GameLocale("field", "Now a lush grassy field is in your sights. The grass is untouched except the small rodents "
                           "that live in it. Flies buzz around your head in the heat.", "You are at the field.",  False,  False, "map")
#VILLAGE
,GameLocale("village", "You can make out what seems to be an old village."
                             "A fire is almost out and spears are lying around.", "You are at the village.",  False,  False, "spear")
#HILLS
,GameLocale("hills", "As the sun glares in your eyes you see that the hills in front of you are rolling everywhere."
                           "Grass is covering the hills and an eagle flys above.", "You are at the hills.",  False,  False, None)
#RIVER
,GameLocale("river", "Water is rushing past you and you gaze upon a giant river."
                           "Swimming through seems to be your only way of crossing", "You are at the river.",  False,  False, None)
#MARSH
,GameLocale("marsh", "You stumble upon a marsh and see ducks flying "
                           "around and a beaver creating a dam", "You are at the marsh.",  False,  False, "axe")
#WATERFALL
,GameLocale("waterfall", "A beautiful waterfall comes into sight and the water sparys your face.  You stare into the beauty that is water falling "
                               "from a cliff and listen to it crash onto the rocks below", "You are at the waterfall.",  False,  False, "canteen")
#DAM
,GameLocale("dam", "A group of beavers is visible and they are constructing a dam. The dam is blocking the water from running freely", "You are at the dam.",  False,  False, "logs")
#POND
,GameLocale("pond", "There appears to be a crystal clear pond with a "
                               "pair of fish swimming side by side", "You are at the pond.",  False,  False, "water")
]

#Intro Dialogue
def naming():
    print("WELCOME TO ISLAND SURVIVAL!")
    userPlayer.name = input(str("Enter your name: "))



def intro():
    print()
    print("Island Survival is a text based game. Controls are: East, "
          "West, North, South, Help, Points, Search, Take, Map, Use, Pray and Quit."
          "On this adventure " + userPlayer.name +  " will enter into many locations. "
          "Hopefully you can make it out alive.")
    print()
    print("You have awoken on a sandy shore with a seagull staring you right "
          "in the face. You rub your eyes and look around. You do not remember "
          "anything except your name:" + userPlayer.name + " and a few other basic skills."
          "Unsure of what to do you start looking around.")
    print()




def main():
    naming()
    intro()
    game()
    endingScene()
    restartFunc()
#Game Function




    
def game():
    global userAction
    global ending
    global useAxe
    global prayers
    prayers = 1
    useAxe = 2
    ending = 99
    useRiver = 1
    
    printLoc(userPlayer.currLoc)
    while True:                     
     if(ending == 2):
         break
     elif userPlayer.moves == 69:
        ending = 1
        break
     elif(ending == 0):
         break
     elif userPlayer.score == 60 and "map" in userPlayer.inven:
         ending = 3
         break
        
  #Using the lifevest at the river      
     elif( useRiver == 1 and userPlayer.currLoc == river):
         print("You fall into the river and dont remember how to swim. You have to be quick. What do you use?")
         userAction = getNextDirection()
         if(userAction == use and cmdItem == "lifevest" and  "lifevest" in userPlayer.inven):
             print("That was a smart move to use the lifevest. You now know that you need it in order to cross the river.")
             useRiver = 0
         else:
            ending = 2
            break
        
     elif(useAxe == 0 and "axe" in userPlayer.inven):
        userPlayer.inven.remove("axe")
        print("The axe broke from using it too much.")    
     
     
     else:
        userAction = getNextDirection()
        if userAction == quit:
            break
        elif userAction == look :
            print(locales[userPlayer.currLoc].loc)
            
        elif userAction == map :
            drawMap()

        elif userAction == search:
            searchForItem(userPlayer.currLoc)

        elif userAction == take:
            takeItem(userPlayer.currLoc)
            
        elif userAction == drop:
            dropItem(userPlayer.currLoc)
            
        elif userAction == use:
            useItem(userPlayer.currLoc)
            
        elif userAction == inventory:
            print(userPlayer.name + "'s Inventory: " + ",".join(str(items) for items in userPlayer.inven) + ".")
        
        elif userAction == help:
            print("Commands are: -North-, -South-, -East- , -West-. -Quit- to end the game, -Look- to look around, -Map- to access map,"
                  " -Search- to search for items, -Take- to take the items after searching, -Drop-, -Use-, -Pray- to get a hint, -Points- to show " + userPlayer.name + "'s score.")
            
        elif userAction == points:
            print("Score: " + str(userPlayer.score) + ".")

        elif userAction == pray:
            prayer()
        
        
        else:
            userPlayer.currLoc = lookUpLoc(userPlayer.currLoc,userAction)
            printLoc(userPlayer.currLoc)
            userPlayer.moves = userPlayer.moves + 1


            

def endingScene():
    global ending
    if (ending == 0):
        print(userPlayer.name + " wins. You have succesfully made it to a safe location with a weapon, fire wood and water to spend the night")
        
    elif(ending  == 1):
        print("You took too long and got caught in the cold of the night. You died. GAME OVER!")
        decide = input("Play again? Yes or No: ")

    elif(ending == 2):
        print("You did not have something to keep you afloat as tried to cross and you drowned. GAME OVER!")
        decide = input("Play again? Yes or No: ")

    elif(ending == 3):
        print("You have been everywhere and you have the map with you. You have seen the island and can survive and navigate!")
        decide = input("Play again? Yes or No: ")

    else:
        print("Thanks for playing!")






#COMMAND FUNCTIONS       
def getNextDirection():
        global cmdItem
        choice = input("Command: ").split(" ")
        cmd = str(choice[0].lower())
        try:
            cmdItem = str(choice[1].lower())
        except:
             cmdItem = " "
             pass
        try:
            return directions.index(cmd)
        except:
            print("Thats not a valid command!")
            return getNextDirection()

        
#Movement        
def lookUpLoc(location, directions):
    if world[location][directions] == None:
       print("There is nothing in that direction.")
       return location
    else:
        return world[location][directions]

    
#PRINTLOC
def printLoc(place):
    
    if(locales[place].beenThere == False):
        print(locales[place].loc)
        userPlayer.score = userPlayer.score + 5
        locales[place].beenThere = True
    else:
        if(userAction == look):
            pass
        else:
            print(locales[place].shortLoc)

            
#SEARCH FUNCTION
def searchForItem(place):
    global itemsLoc
    global cmdItem
    userPlayer.moves = userPlayer.moves + 1
    locales[place].examThere = True
    if locales[place].items != None:
        print("Look a(n) " + locales[place].items)  
    else:
        print("Nothing here.")

        
#TAKE FUNCTION
def takeItem(place):
    global itemsLoc
    global cmdItem
    userPlayer.moves = userPlayer.moves + 1
    if locales[place].examThere == False: #make sure you search first
        print("You need to search for an item first!")
    else:
        if locales[place].items == None:
            print("I guess there is nothing here.")
        else:
            if(cmdItem == " "):
                print("You need to take a specific item.")
            elif(cmdItem == locales[place].items): #Seeing item is there to take
                if(userPlayer.currLoc == forest or userPlayer.currLoc == dam or userPlayer.currLoc == pond):
                    print("You need to use a specific item here to take it")
                else:
                    userPlayer.inven.append(locales[place].items) 
                    print("Congrats, You took a " + locales[place].items + ".")
                    locales[place].items = None
        
            else:
                print("That item is not here")

#DROP FUNCTION
def dropItem(place):
    userPlayer.moves = userPlayer.moves + 1
    if(cmdItem == " "):#make sure you put what you want to drop
        print("You need to drop a specific item.")
    elif cmdItem in userPlayer.inven:
        if(locales[place].items  != None):
            print("There is already an item at this location")
        else:
            userPlayer.inven.remove(cmdItem) 
            print("You dropped a " + cmdItem+ ".")
            locales[place].items = cmdItem
    else:
        print("That item is not in your inventory")


#USE FUNCTION
def useItem(place):
    global itemsLoc
    global cmdItem
    global ending
    global useAxe
    
    userPlayer.moves = userPlayer.moves +1
    if(cmdItem == " "): # if they dont say what item
        print("You need to use a specific item." )
    else:
        if cmdItem in userPlayer.inven: #make sure they have it
            
            if place == cave and "spear" in userPlayer.inven and "wood" in userPlayer.inven and "water" in userPlayer.inven:
                ending = 0
            
            elif(place == forest and "axe" in userPlayer.inven):
                 print("You got dry wood to make a fire.")
                 userPlayer.inven.append("wood")
                 useAxe = useAxe -1
                 locales[place].items = None
                 
                 
                 
            elif(place == dam and "axe" in userPlayer.inven):
                 print("You got wet logs. That wont help make a fire")
                 userPlayer.inven.append("logs")
                 useAxe = useAxe -1
                 locales[place].items = None

            elif(place == pond and "canteen" in userPlayer.inven):
                 print("You got water.")
                 userPlayer.inven.append("water")
                 locales[place].items = None
                 
                 
                                
            else:
                print("You cant use that item here")
        else:
            print("You do not have that item.")
    
                
        
        
        

#Map Of Island
def drawMap():
  if "map" in userPlayer.inven:
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
        print("              |            | ")
        print("              |            | ")
        print("              |            | ")
        print("            Dam----------Pond")
  else:
       print("You do not have a map with you.")

def restartFunc():
    restart = input("Do you want to play again? ")
    if restart.lower() == "yes":
        #Reset player values
        userPlayer.inven = []
        userPlayer.score = 0
        userPlayer.moves = 0
        userPlayer.currLoc = beach
        userPlayer.name = ""
        for places in locales:
             places.beenThere = False
             places.examThere = False
             places.items = None

        locales[0].items = "lifevest"
        locales[3].items = "wood"
        locales[4].items = "map"
        locales[5].items = "spear"
        locales[8].items = "axe"
        locales[9].items = "canteen"
        locales[10].items = "logs"
        locales[11].items = "water"
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\nResetting Game..."
              "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")#Making sure people cant see old games that have been played
        main()
    elif restart.lower() == "no":
        print("Thanks for playing!")
        quit
    else:
        print("Please Enter -Yes- or -No-")
        restartFunc()

def prayer():
    global prayers
    if(prayers == 1):
        if( "map" in userPlayer.inven):
            print("The air swirls around you and a ghostly figure appears."
              "He says to you in a low wispy voice: Cave...Safety. The air becomes dead and he disappears.")
            prayers = prayers - 1
        elif( "lifevest" not in userPlayer.inven):
            print("The air swirls around you and a ghostly figure appears."
              "He says to you in a low wispy voice: Do not drown in the river. The air becomes dead and he disappears.")
            prayers = prayers - 1
        else:
            print("The air swirls around you and a ghostly figure appears."
              "He says to you in a low wispy voice: The field will bring you in the right direction. The air becomes dead and he disappears.")
            prayers = prayers - 1       
    else:
        print("You already prayed.")
    
    


                       
main()

print("Copyright: Jake Tantorski jake.tantorski1@marist.edu ")


