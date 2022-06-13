# Object Oriented Programming

class Dog:
    
    # Attributes of class
    def __init__(self, name, age, breed):
        self.name = str(name)
        self.age = int(age)
        self.breed = str(breed)
    
    # Functions inside the class are methods 
    def bark(self):
        print("woof woof")
        
    def emoji(self):
        print("🐶")
    
    def Name(self):
        return self.name
    
    def Age(self):
        return self.age
    
    def Breed(self):
        return self.breed
    
    def changeAge(self, age):
        self.age = age

d = Dog("Jax",4, "Jack Russell Terrier")

print(type(d))

d.Name()
d.Age()
d.Breed()

d.emoji()

d1 = Dog("Demon", 8, "Siberian Husky")

d1.Name()
d1.Age()
d1.Breed()


# Changing age 
d.changeAge(5)
d1.changeAge(9)

d.Age()
d1.Age()



# Inheritance

class cat(Dog):
    
    def __init__(self, name, age, breed):
        self.name = str(name)
        self.age = int(age)
        self.breed = str(breed)
        
Kitty = cat("Chotu", 5, "Stray")

Kitty.emoji()


# Inheritance refined + Polymorphism

class animals():
    
    def __init__(self, name, age, species):
        self.name = str(name)
        self.age = int(age)
        self.species = str(species)
    
    def Name(self):
        return self.name
    
    def Age(self):
        return self.age
    
    def species(self):
        return self.species
    
class Dogs(animals):
    
    def bark(self):
        print("woof woof")
    
    def emoji(self):
        print("🦮")

class Cats(animals):
    
    def meow(self):
        print("meow meow")
    
    def emoji(self):
        print("🐱")
        

kitty_cat = Cats("Chimmy",8,"Mammal")

doggy_dog = Dogs("Ducchi",8,"Mammal")

kitty_cat.emoji()
kitty_cat.Name()

doggy_dog.emoji()
doggy_dog.Name()


