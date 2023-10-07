class Animal:
    def __init__(self, name):
        self.name: name
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog(name = "Betty")
cat = Cat(name = "Kitty")

dog.speak()
cat.speak()