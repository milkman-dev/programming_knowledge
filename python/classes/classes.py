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

class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter):
    print(f"New circle with diameter: {diameter}")

teaching_table = Circle(36)

''' Just as there are class variables (class attributes) 
we can also have instance variables (instance attributes)'''
