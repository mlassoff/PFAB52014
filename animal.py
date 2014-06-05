class Animal:
	'This class is designed to represent real world animals'
	numAnimals = 0

	def __init__(self, name, length, weight, color, soundItMakes):
		self.name = name
		self.length = length
		self.weight = weight
 		self.color = color
		self.soundItMakes = soundItMakes
		Animal.numAnimals += 1

	def eat(self):
		print self.name ," is eating"

	def sleep(self):
		print self.name, "is sleeping"

	def run(self):
		print self.name, "is running"

					
#kitty = Animal("Meowser", 18, 5, "Gray" , "Meow")
#kitty.eat()
#kitty.sleep()
#kitty.run()

#doggy = Animal("Rover" , 36, 48, "Brown" , "Woof")
#doggy.eat()
#doggy.sleep()
#doggy.run()
	
