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
self=pet(name_pet, 50, 50,50,50,100)
self = pet(name_pet)
petstat= [self.hunger, self.thirst, self.happiness, self.love, self.money]
print (self. __dict__)
while True:
    options = ["1","2","3","4","5"]
    activity= input ("1:play or 2:feed or 3:water or 4:care 5:slot machine")
    def hungry():
        self.hunger += 10
        self.happiness -=2
        self.love -=2
        self.thirst -=2
        self.money += 10

    def happiness():
        self.happiness += 10
        self.hunger -=2
        self.love -=2
        self.thirst -=2
        self.money += 10

    def water():
        self.thirst += 10
        self.hunger -=2
        self.love -=2
        self.happiness-=2
        self.money += 10

    def love():
        self.love += 10
        self.happiness -=2
        self.hunger-=2
        self.money += 10
        self.thirst -=2

    def overcap():
        for stat in ("hunger", "love", "thirst", "happiness"):
            setattr(self, stat, min(getattr(self, stat), 100))
            
    def gamble():
        slot=random.randint(7,77)
        self.money -=7
        if slot == 77:
            print("YOU WON BIG KEEP GOING DUDE")
            self.money += 777

    def checkdeath():
        if self.hunger <=0:
            print (f"{name_pet} was not fed, it died")
        elif self.love <=0:
            print(f"{name_pet} was uncared for, it ran away")
            exit()
        elif self.happiness <=0:
            print(f"{name_pet} was despressed it lowkey might be dead")
            exit()
        elif self.thirst <=0:
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

    print(f"{name_pet}'s stats: Happiness:{self.happiness} Hunger:{self.hunger} Thirst:{self.thirst} Love:{self.love} Cash:{self.money}")












