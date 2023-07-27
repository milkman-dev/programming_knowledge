''' There are different programming languages, python is an OOP (Objected oriented programming) 
language this means that we can make "objects" which are basically data types that we create, this
are called "CLASSES"'''

# To define a class we begin with the class keyword

class My_class:
    pass # pass keyword is used so that the terminal doesn't print an error

''' Classes can have methods (functions inside the class) 
and also attributes (variables) inside'''
def my_method(self): # Methods must at least have the "self" argument which holds the instantiation of the class
    pass

''' Classes can also have attributes (variables) 
this are called "class attributes"'''
class Grade():
  minimum_passing = 65 # This is the attribute

''' Class methods can have more than 1 argument 
(remember there is 1 default argument "self")'''
class Circle:
  pi = 3.14

  def area(self, radius):
    return self.pi * radius ** 2

circle = Circle()

pizza_area = circle.area(12 / 2) # We just call the method with 1 argument because "self" is the instance
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

''' There are special methods which are called "constructors" 
these things are called by default everytime a class instance is created'''

class Circle1:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

teaching_table = Circle1(36)

''' Just as there are class variables (class attributes) 
we can also have instance variables (instance attributes)'''
class Store:
  pass # Notice there are no class attributes

alternative_rocks = Store() # We create 2 instances
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks" # We add a instance variable
isabelles_ices.store_name = "Isabelle's Ices"

# There can be also attribute functions remember the .count() method?

can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for element in can_we_count_it:
  if hasattr(element, "count"):
    print(str(type(element)) + " has the count attribute!")
  else:
    print(str(type(element)) + " does not have the count attribute :(")

# More about "Self" and attributes and methods

class Circle:
  pi = 3.14
  
  def __init__(self, diameter): # We specify that when initiating the instance a diameter must be specified
    print(f"Creating circle with diameter {diameter}")
    # Add assignment for self.radius here:
    self.radius = diameter / 2
  
  def circumference(self):
    return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

''' There is another method that can help us print something to represent
the class, so that when we print the class instead of watching the memory
location something else is printed'''

class Employee():
  def __init__(self, name):
    self.name = name
 
  def __repr__(self): # This is the represent method
    return self.name
 
argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"