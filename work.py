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
    def __init__(self, name, happiness, hunger, inventory):
        self.name = name 
        self.happiness = int(happiness)
        self.hunger = int(hunger)
        self.inventory = [inventory]

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)
Namepet= input("Name pet")
Pet = pet(Namepet, 50, 50)
Pet.buy({"title": "Food", "hunger":10})



 