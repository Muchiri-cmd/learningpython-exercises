class Car():
  #A simple attempt to represent a car.
  def __init__(self, make, model, year):
   """Initialize attributes to describe a car."""
   self.make = make
   self.year = year
   self.model=model
   self.odometer_reading=0
 
  def get_descriptive_name(self):
   """Return a neatly formatted descriptive name."""
   long_name = str(self.year) + ' ' + self.make + ' ' + self.model
   return long_name.title()
   
  def read_odometer(self):
   """Print a statement showing the car's mileage."""
   print("This car has " + str(self.odometer_reading) + " miles on it.")
   
  def update_odometer(self, mileage):
   """Set the odometer reading to the given value."""
   self.odometer_reading = mileage
 
my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.update_odometer(80)
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
