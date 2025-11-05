""" class Hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Jillian = Hero("Jillian", 150, ["Potion"])
Jillian.buy({"title": "Sword", "atk": 34})
print(Jillian.__dict__)
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # double underscore means "private"

    def deposit(self, amount):
        self.__balance += amount

    def show_balance(self):
        print(f"{self.owner} has ${self.__balance}")

    
 """
class pet:
    while True:
        def __init__(self, name , happiness):
            self.name = name 
            self.happiness = happiness 
        happiness = 0
        play=(input("play with bro?"))

        if play.lower == "yes":
            happiness +=10
            print("Pet is now playing")
            print(happiness)
        if play.lower == "no":
            continue
