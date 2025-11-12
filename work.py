# """ """ class Hero:
#     def __init__(self, name, money, inventory):
#         self.name = name
#         self.money = money
#         self.inventory = inventory

#     def buy(self, item):
#         self.inventory.append(item)
#         print(self.inventory)

# Jillian = Hero("Jillian", 150, ["Potion"])
# Jillian.buy({"title": "Sword", "atk": 34})
# print(Jillian.__dict__) """
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # double underscore means "private"

#     def deposit(self, amount):
#         self.__balance += amount

#     def show_balance(self):
#         print(f"{self.owner} has ${self.__balance}")

    
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
    activity= input ("play or feed or give water or care")
    if activity.lower() == "feed":
        Pet.hunger += 10
    if Pet.hunger > 100:
        Pet.hunger = 100 
        print("pet is full")
    print(f"Hunger:", (Pet.hunger))

    if activity.lower() == "play":
        Pet.happiness += 10
    if Pet.happiness > 100:
        Pet.happiness = 100 
        print("Pet is super happy")
    print(f"Happiness:", (Pet.happiness))
    
    if activity.lower() == "give water":
        Pet.thirst += 10
    if Pet.thirst > 100:
        Pet.thirst = 100 
        print("pet is vanquished of its thirst")
    print(f"Thirst:", (Pet.thirst))

    if activity.lower() == "care":
        Pet.love += 10
    if Pet.love > 100:
        Pet.love = 100 
        print("pet feels loved for")
    print(f"Love:", (Pet.love))

    
    if activity.lower() == "no":
        continue


 