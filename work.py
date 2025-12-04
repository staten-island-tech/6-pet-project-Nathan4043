import random
name_pet = input("name the pet")
class pet:
    def __init__(self, name, happiness, hunger, thirst, love, money ):
        self.name = name
        self.happiness = int(happiness)
        self.hunger = int(hunger)
        self.thirst = int(thirst)
        self.love = int(love)
        self.money = int(money)
slot=random.randint(1,10)
Pet = pet(name_pet, 50, 50,50,50,100)
petstat= [Pet.hunger, Pet.thirst, Pet.happiness, Pet.love, Pet.money]
print (Pet. __dict__)
while True:
    options = ["1","2","3","4","5"]
    activity= input ("1:play or 2:feed or 3:water or 4:care 5:slot machine")
    def hungry():
        Pet.hunger += 10
        Pet.happiness -=2
        Pet.love -=2
        Pet.thirst -=2
        Pet.money += 10

    def happiness():
        Pet.happiness += 10
        Pet.hunger -=2
        Pet.love -=2
        Pet.thirst -=2
        Pet.money += 10

    def water():
        Pet.thirst += 10
        Pet.hunger -=2
        Pet.love -=2
        Pet.happiness-=2
        Pet.money += 10

    def love():
        Pet.love += 10
        Pet.happiness -=2
        Pet.hunger-=2
        Pet.money += 10
        Pet.thirst -=2

    def overcap():
        for stat in ("hunger", "love", "thirst", "happiness"):
            setattr(Pet, stat, min(getattr(Pet, stat), 100))
    def gamble():
        slot=random.randint(7,77)
        Pet.money -=7
        if slot == 77:
            print("YOU WON BIG KEEP GOING DUDE")
            Pet.money += 777

    def checkdeath():
        if Pet.hunger <=0:
            print (f"{name_pet} was not fed, it died")
        elif Pet.love <=0:
            print(f"{name_pet} was uncared for, it ran away")
            exit()
        elif Pet.happiness <=0:
            print(f"{name_pet} was despressed it lowkey might be dead")
            exit()
        elif Pet.thirst <=0:
            print(f"{name_pet} was not given water, pet is dried up like a raisin")
            exit()
        elif activity.lower() == "5":
            gamble()

    actions = {
        "1": happiness,
        "2": hungry,
        "3": water,
        "4": love,
        "5": gamble,
    }
    choice = activity.lower()
    if choice in actions:
        actions[choice]()
    else:
        print ("Wrong option, Choose again")
        continue

    overcap()
    checkdeath()

    print(f"{name_pet}'s stats: Happiness:{Pet.happiness} Hunger:{Pet.hunger} Thirst:{Pet.thirst} Love:{Pet.love} Cash:{Pet.money}")
        
    
      












