class Animal:
    def move(self):
        print("Animals can move")

class Dog(Animal):
    def move(self):
        print("The dog runs")

class Bird(Animal):
    def move(self):
        print("The bird flies")

class Vehicle:
    def move(self):
        print("Vehicles can move")

class Car(Vehicle):
    def move(self):
        print("The car drives")

class Plane(Vehicle):
    def move(self):
        print("The plane flies")

creatures = [Dog(), Bird(), Car(), Plane()]

for creature in creatures:
    creature.move()

