#Jake Tantorski CMPT 120L 


score = 0


rocks = ("You stumble upon a rocky surface. The is no life to be seen and water is scarce")
beach = ("A beach appears. Waves crash against the sandy beach and palm trees sway in the wind")
cave = ("Between sime bushes a cave is visible. You walk inside and see many drawings on the wall and a torch lit in the back")
forest = ("A thick forest appears with many tall luming trees. Aniamls are abdunant and you smell pine")
field = ("Now a lush grassy field is in your sights. The grass is untouched except the small rodents that live in it. Flies buzz around your head in the heat")
village = ("You can make out what seems to be an old village. A fire is almost out and spears are lying around")


title = ("Welcome to The Pursuit of Happiness. On this adventure you will enter into many locations. Hopefully you can make it out alive")
def intro():
    print(title)
    intro.name = input(str("Enter your name: "))
intro()

def game():
    myLoc = beach
    print(myLoc)
    


    if(myLoc == rocks):
        direction = input("South or East")
        if(direction == "South"):
            myLoc= beach
            print(beach)
        elif(direction == "East"):
            myLoc = cave
            print(cave)

    if(myLoc == cave):
        direction = input("West or South")
        if(direction == "West"):
            myLoc= rocks
            print(rocks)
        elif(direction == "South"):
            myLoc = forest
            print(forest)

    if(myLoc == beach):
        direction = input("North, East or South")
        if(direction == "North"):
            myLoc= rocks
            print(rocks)
        elif(direction == "South"):
            myLoc = village
            print(village)
        elif(direction == "East"):
            myLoc = forest
            print(forest)
            
            
game()

            
    
        





'''input()
myLocation = beach
print(myLocation)
score = score + 5
print (name + "'s score is: "  + str(score) + "  -Press Enter")
print()

input()
myLocation = cave
print(myLocation)
score = score + 5
print (name + "'s score is: "  + str(score) + "  -Press Enter")
print()

input()
myLocation = forest
print(myLocation)
score = score + 5
print (name + "'s score is: "  + str(score) + "  -Press Enter")
print()
           
input()
myLocation = village
print(myLocation)
score = score + 5
print (name + "'s score is: "  + str(score) + "  -Press Enter")
print()

       
input()
myLocation = field
print(myLocation)
print("Youve been everywhereit seems like. You think back on the day you've had. You could've never imagined seeing these places and having these things happen to you but you are thankful you get to see another day on the island.")
score = score + 5
print (name + "'s score is: "  + str(score) + "  -Press Enter")
print("Copyright: Jake Tantorski jake.tantorski1@gmail.com")'''


