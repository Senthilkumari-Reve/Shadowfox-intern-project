# Create an Avenger Class
'''1.Create a class Avenger
   2.store these attributes for each superheros
   *Name
   *Age
   *Gender
   *Super Power
   *Weapon
   3.create a method to display their info
   4,Create a method is_leader() to check if the hero is a leader

   Superheros List:
   super_heroes = ["Captain America", "Iron Man", "Black Widow", "Hulk", "Thor", "Hawkeye"]

   '''

class Avenger:
    def __init__(self, name, age, gender, super_power, weapon):
        self.name = name
        self.age = age
        self.gender = gender
        self.super_power = super_power
        self.weapon = weapon

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Super Power: {self.super_power}")
        print(f"Weapon: {self.weapon}")
        print()

    def is_leader(self):
        return self.name == "Captain America"

# Creating Avenger objects
avengers = [
    Avenger("Captain America", 100, "Male", "Super strength", "Shield"),
    Avenger("Iron Man", 48, "Male", "Technology", "Armor"),
    Avenger("Black Widow", 35, "Female", "Superhuman", "Batons"),
    Avenger("Hulk", 40, "Male", "Unlimited Strength", "No Weapon"),
    Avenger("Thor", 1500, "Male", "Super Energy", "Mjölnir"),
    Avenger("Hawkeye", 38, "Male", "Fighting Skills", "Bow and Arrows")
]

# Display info for each avenger
for hero in avengers:
    hero.display_info()
    if hero.is_leader():
        print(f"{hero.name} is the leader of the Avengers.\n")
