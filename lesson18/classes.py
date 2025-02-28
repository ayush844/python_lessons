# ----------------------------- CLASS AND OBJECTS -----------------------------
# A class is a blueprint for creating objects. It defines properties (attributes) and behaviors (methods).
# An object is an instance of a class.

class Vehicle:
    """A base class for different types of vehicles."""
    
    def __init__(self, make, model):
        """
        Constructor method (__init__):
        - Initializes the attributes 'make' and 'model' when a Vehicle object is created.
        - 'self' refers to the instance of the class.
        """
        self.make = make  # Make of the vehicle (e.g., Tesla, Ford)
        self.model = model  # Model of the vehicle (e.g., Model 3, Mustang)

    def moves(self):
        """Defines a generic movement behavior for a vehicle."""
        print('Moves along..')

    def get_make_model(self):
        """Prints the make and model of the vehicle."""
        print(f"I'm a {self.make} {self.model}.")


# Creating an instance (object) of the Vehicle class
my_car = Vehicle('Tesla', 'Model 3')

# Accessing attributes (commented-out print statements would print the values)
# print(my_car.make)   # Output: Tesla
# print(my_car.model)  # Output: Model 3

# Calling methods on the object
my_car.get_make_model()  # Output: I'm a Tesla Model 3.
my_car.moves()           # Output: Moves along..

# Creating another Vehicle object
your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()  # Output: I'm a Cadillac Escalade.
your_car.moves()           # Output: Moves along..


# ----------------------------- INHERITANCE -----------------------------
# Inheritance allows a class to inherit properties and behaviors from another class.
# A child class (subclass) can override methods of its parent class.

class Airplane(Vehicle):
    """Airplane class inherits from Vehicle."""
    
    def __init__(self, make, model, faa_id):
        """
        Extends the Vehicle class by adding an additional attribute 'faa_id' (Flight ID).
        'super().__init__(make, model)' calls the constructor of the Vehicle class.
        """
        super().__init__(make, model)  # Call parent constructor
        self.faa_id = faa_id  # FAA ID is specific to airplanes

    def moves(self):
        """Overrides the 'moves' method of the parent class to define airplane-specific movement."""
        print('Flies along..')


class Truck(Vehicle):
    """Truck class inherits from Vehicle."""
    
    def moves(self):
        """Overrides the 'moves' method to define truck-specific movement."""
        print('Rumbles along..')


class GolfCart(Vehicle):
    """GolfCart class inherits from Vehicle but does not override methods."""
    pass  # Inherits everything from Vehicle without modification


# ----------------------------- OBJECT CREATION -----------------------------
# Creating instances of different classes

cessna = Airplane('Cessna', 'Skyhawk', 'N-12345')  # Airplane object
mack = Truck('Mack', 'Pinnacle')  # Truck object
golfwagon = GolfCart('Yamaha', 'GC100')  # GolfCart object

# Calling methods on Airplane object
cessna.get_make_model()  # Output: I'm a Cessna Skyhawk.
cessna.moves()           # Output: Flies along..

# Calling methods on Truck object
mack.get_make_model()  # Output: I'm a Mack Pinnacle.
mack.moves()           # Output: Rumbles along..

# Calling methods on GolfCart object
golfwagon.get_make_model()  # Output: I'm a Yamaha GC100.
golfwagon.moves()           # Output: Moves along.. (Inherited from Vehicle, no override)


# ----------------------------- POLYMORPHISM -----------------------------
# Polymorphism allows different classes to define the same method but with different behaviors.

print('\n\n')

# Loop through different vehicle objects and call common methods
for v in (my_car, your_car, cessna, mack, golfwagon):
    v.get_make_model()  # Calls the method defined in Vehicle
    v.moves()           # Calls overridden methods if present, otherwise uses Vehicle's method

# I'm a Tesla Model 3.
# Moves along..
# I'm a Cadillac Escalade.
# Moves along..
# I'm a Cessna Skyhawk.
# Flies along..
# I'm a Mack Pinnacle.
# Rumbles along..
# I'm a Yamaha GC100.
# Moves along..