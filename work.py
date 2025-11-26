import random
class pet:
    def __init__(self, name, happiness, hunger, thirst, love, money ):
        self.name = name 
        self.happiness = int(happiness)
        self.hunger = int(hunger)
        self.thirst = int(thirst)
        self.love = int(love)
        self.money = int(money)
slot=random.randint(1,10)
Pet = pet("pet", 50, 50,50,50,100)
Pet.buy({"title": "Food", "hunger":10})
print (Pet. __dict__)
while True:
    activity= input ("1:play or 2:feed or 3:water or 4:care 5:slot machine")

    if activity.lower() == "1":
        Pet.hunger += 10
        Pet.happiness -=2
        Pet.love -=2
        Pet.thirst -=2
        Pet.money += 10
    if Pet.hunger > 100:
        Pet.hunger = 100 
    if Pet.hunger <=0:
        print("pet was unfed and died")
        exit()

    if activity.lower() == "2":
        Pet.happiness += 10
        Pet.hunger -=2
        Pet.love -=2
        Pet.thirst -=2
        Pet.money += 10
    if Pet.happiness > 100:
        Pet.happiness = 100 
    if Pet.happiness <=0:
        print("pet was despressed he lowkey might be dead")
        exit()

    if activity.lower() == "3":
        Pet.thirst += 10
        Pet.hunger -=2
        Pet.love -=2
        Pet.happiness-=2
        Pet.money += 10
    if Pet.thirst > 100:
        Pet.thirst = 100 
    if Pet.thirst <=0:
        print("pet was not given water, pet is dried up like a raisin")
        exit()

    if activity.lower() == "4":
        Pet.love += 10
        Pet.happiness -=2
        Pet.hunger-=2
        Pet.money += 10
        Pet.thirst -=2
    if Pet.love > 100:
        Pet.love = 100
    if Pet.love <=0:
        print("pet was uncared for, it ran away")
        exit()
    print(f"Hunger: {Pet.hunger}")
    print(f"Happiness: {Pet.happiness}")
    print(f"Thirst: {Pet.thirst}")
    print(f"Love: {Pet.love}")
    print(f"Money$:{Pet.money}")
    if activity.lower() == "no":
        continue
    if activity.lower() == "5":
    
    
      












