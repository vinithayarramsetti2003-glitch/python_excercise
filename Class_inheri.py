class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of Doors: {self.num_doors}")

car1 = Car("Toyota", "Corolla", 4)
car1.display_info()
	

synopses:
ex–9: oop – class and inheritance
a base class vehicle is created with attributes for make and model. a subclass car extends it by adding a new attribute, num_doors, and a method to display all details. this exercise demonstrates the concept of inheritance and object-oriented programming.
.

