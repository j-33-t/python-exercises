# OOP Exercise 1: Create a Class with instance attributes
# Write a Python program to create a Vehicle class with "name", "max_speed" and "mileage" instance attributes.

class Vehicle():
    def __init__(self,name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        
Tesla_model_X = Vehicle(200,30)

print(f" max_speed : {Tesla_model_X.max_speed} , mileage : {Tesla_model_X.mileage}")

# OOP Exercise 3: Create a child class Bus 
# that will inherit all of the variables and methods of the Vehicle class
# Expected output : "Vehicle Name: School Volvo Speed: 180 Mileage: 12"

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 180, 12) 

print(f"Vehicle Name: {school_bus.name} Speed : {school_bus.max_speed} Mileage : {school_bus.mileage} ")