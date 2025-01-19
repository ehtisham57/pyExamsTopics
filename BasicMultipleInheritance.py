# Multiple inheritance

class Animal:
    def speak(self):
        print("Animal makes a sound.")

class Bird:
    def fly(self):
        print("Bird can fly.")

class Bat(Animal, Bird):
    pass

# Values
bat = Bat()
bat.speak()
bat.fly()  