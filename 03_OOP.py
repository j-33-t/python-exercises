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

d1 = Dog("Demon", 8, "Siberian Husky")

d1.Name()
d1.Age()
d1.Breed()


# Changing age 
d.changeAge(5)
d1.changeAge(9)

d.Age()
d1.Age()



# Multiple classes