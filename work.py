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
        if Pet.hunger > 100:
            Pet.hunger = 100
        if Pet.love > 100:
            Pet.love = 100
        if Pet.thirst > 100:
            Pet.thirst = 100
        if Pet.happiness > 100:
            Pet.happiness = 100
    def gamble():
        slot=random.randint(7,77)
        Pet.money -=7
        if slot == 77:
            print("YOU WON BIG KEEP GOING DUDE")
            Pet.money += 777

    def checkdeath():
        if Pet.hunger <=0:
            print (f"{name_pet} was not fed, it died")
        if Pet.love <=0:
            print(f"{name_pet} was uncared for, it ran away")
            exit()
        if Pet.happiness <=0:
            print(f"{name_pet} was despressed it lowkey might be dead")
            exit()
        if Pet.thirst <=0:
            print(f"{name_pet} was not given water, pet is dried up like a raisin")
            exit()
        if Pet.money <= 0:
            print("dawg, you in cripping debt")
            exit()
    
    overcap()
    checkdeath()

    if activity.lower() == "1":
        happiness()

    elif activity.lower() == "2":
        hungry()

    elif activity.lower() == "3":
        water()

    elif activity.lower() == "4":
        love()
    
    elif activity.lower() == "5":
        slot=random.randint(7,77)
        Pet.money -=5
        if slot == 77:
            print("YOU WON BIG KEEP GOING DUDE")
            Pet.money += 777

    elif activity not in options:
        print("Wrong option, Choose again")
        continue

    overcap()
    checkdeath()

    if activity.lower() == "5":
        slot=random.randint(7,77)
        Pet.money -=5
        if slot == 77:
            print("YOU WON BIG KEEP GOING DUDE")
            Pet.money += 777

    print(f"{name_pet}'s stats: Happiness:{Pet.happiness} Hunger:{Pet.hunger} Thirst:{Pet.thirst} Love:{Pet.love} Cash:{Pet.money}")
        
    
      












