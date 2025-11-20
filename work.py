
class pet:
    def __init__(self, name, happiness, hunger, thirst, love, inventory):
        self.name = name 
        self.happiness = int(happiness)
        self.hunger = int(hunger)
        self.thirst = int(thirst)
        self.love = int(love)
        self.inventory = [inventory]

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Pet = pet("pet", 50, 50,50,50, [])
Pet.buy({"title": "Food", "hunger":10})
print (Pet. __dict__)
while True:
    activity= input ("1:play or 2:feed or 3:water or 4:care")

    if activity.lower() == "1":
        Pet.hunger += 10
        Pet.happiness -=2
        Pet.love -=2
        Pet.thirst -=2
    if Pet.hunger > 100:
        Pet.hunger = 100 
        print("pet is full")
    if Pet.hunger ==0:
        print("pet was unfed and died")
        exit()

    if activity.lower() == "2":
        Pet.happiness += 10
        Pet.hunger -=2
        Pet.love -=2
        Pet.thirst -=2
    if Pet.happiness > 100:
        Pet.happiness = 100 
        print("Pet is super happy")
    if Pet.happiness ==0:
        print("pet was despressed he lowkey might be dead")
        exit()

    if activity.lower() == "3":
        Pet.thirst += 10
        Pet.hunger -=2
        Pet.love -=2
        Pet.happiness-=2
    if Pet.thirst > 100:
        Pet.thirst = 100 
        print("pet is vanquished of its thirst")
    if Pet.thirst ==0:
        print("pet was not given water, pet is dried up like a raisin")
        exit()

    if activity.lower() == "4":
        Pet.love += 10
        Pet.happiness -=2
        Pet.hunger-=2
        Pet.thirst -=2
    if Pet.love > 100:
        Pet.love = 100
        print("pet feels loved for")
    if Pet.love ==0:
        print("pet was uncared for, it ran away")
        exit()

    if Pet.hunger < 0: Pet.hunger = 0
    if Pet.happiness < 0: Pet.happiness = 0
    if Pet.thirst < 0: Pet.thirst = 0
    if Pet.love < 0: Pet.love = 0
    
    print(f"Hunger: {Pet.hunger}")
    print(f"Happiness: {Pet.happiness}")
    print(f"Thirst: {Pet.thirst}")
    print(f"Love: {Pet.love}")
    if activity.lower() == "no":
        continue
    items =[
        {
            "name": "Whole pizza"
            "stat": 50 
        }
    ]   
    if activity.lower() == "shop":


        "Whole pizza:50 hunger","Water Jug: 50 thirst","Awesome ball: 50 Happiness","Brush:50 Care/love","Slot machine(pick this plsplspslpsls): gmable"