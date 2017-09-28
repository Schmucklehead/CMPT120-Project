#Jake Tantorski CMPT 120L 

global score
score = 0




rocks = ("You stumble upon a rocky surface. The is no life to be seen and water is scarce")
beach = ("A beach appears. Waves crash against the sandy beach and palm trees sway in the wind")
cave = ("Between some bushes a cave is visible. You walk inside and see many drawings on the wall and a torch lit in the back")
forest = ("A thick forest appears with many tall luming trees. Aniamls are abdunant and you smell pine")
field = ("Now a lush grassy field is in your sights. The grass is untouched except the small rodents that live in it. Flies buzz around your head in the heat")
village = ("You can make out what seems to be an old village. A fire is almost out and spears are lying around")


beenThereRocks = False
beenThereBeach = False
beenThereCave = False
beenThereForest = False
beenThereField = False
beenThereVillage = False

myLoc = beach

title = ("Welcome to The Pursuit of Happiness. On this adventure you will enter into many locations. Hopefully you can make it out alive. You start a beach")
def intro():
    print(title)
    intro.name = input(str("Enter your name: "))
intro()

def game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage):
 
    print(myLoc, "Your score is ", score)
    

    
    if(myLoc == rocks):
        direction = input("South or East: ")
        if(direction == "South"):
            myLoc= beach
            if(beenThereBeach == False):
                score = score + 5
                beenThereBeach = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "East"):
            myLoc = cave
            if(beenThereCave == False):
                score = score + 5
                beenThereCave = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        else:
            print("No")
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
            

    if(myLoc == cave):
        direction = input("West or South: ")
        if(direction == "West"):
            myLoc= rocks
            if(beenThereRocks == False):
                score = score + 5
                beenThereRocks = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "South"):
            myLoc = forest
            if(beenThereForest == False):
                score = score + 5
                beenThereForest = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        else:
            print("No")
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)

    if(myLoc == beach):
        direction = input("North, East or South: ")
        if(direction == "North"):
            myLoc= rocks
            if(beenThereRocks == False):
                score = score + 5
                beenThereRocks = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "South"):
            myLoc = village
            if(beenThereVillage == False):
                score = score + 5
                beenThereVillage = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "East"):
            myLoc = forest
            if(beenThereForest == False):
                score = score + 5
                beenThereForest = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "West"):
            myLoc = field
            if(beenThereField == False):
                score = score + 5
                beenThereField = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        else:
            print("No")
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)


    if(myLoc == field):
        direction = input("East or South: ")
        if(direction == "South"):
            myLoc = village
            if(beenThereVillage== False):
                score = score + 5
                beenThereVillage = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "East"):
            myLoc = beach
            if(beenThereBeach == False):
                score = score + 5
                beenThereBeach = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        else:
            print("No")

    if(myLoc == village):
        direction = input("North or West: ")
        if(direction == "North"):
            myLoc= beach
            if(beenThereBeach == False):
                score = score + 5
                beenThereBeach = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "West"):
            myLoc = field
            if(beenThereField == False):
                score = score + 5
                beenThereField = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        else:
            print("No")
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage )

    if(myLoc == forest):
        direction = input("North or South: ")
        if(direction == "North"):
            myLoc= cave
            if(beenThereCave== False):
                score = score + 5
                beenThereCave = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "South"):
            myLoc = village
            if(beenThereVillage == False):
                score = score + 5
                beenThereVillage = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        elif(direction == "West"):
            myLoc = beach
            if(beenThereBeach == False):
                score = score + 5
                beenThereBeach = True
            else:
                pass
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        else:
            print("No")
            game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)
        
    
            
game(myLoc,score,beenThereRocks, beenThereBeach, beenThereCave, beenThereForest, beenThereField, beenThereVillage)




    
    
        





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


