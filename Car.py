class Car:
	'This class is simulating a car'

	def __init__(self, carId, name, direction, speed):
		self.carId = carId
		self.name = name
		self.direction = direction
		self.speed = speed

	def accelerate(self):
		if self.speed < 65:
			self.speed += 1
		else:
			print "Top Speed Reached"		

	def brake(self):
		if self.speed > 0:
			self.speed -=1
		else:
			print "You are already stopped"

	def turnLeft(self):
		if self.direction == 0:
			self.direction= 350
		else:
			self.direction -= 10

	def turnRight(self):
		if self.direction < 360:
			self.direction += 10
		else:
			self.direction = 0	
	
	def carStatus(self):
		print "Status of ", self.carId
		print "Car Name: " , self.name
		print "Heading: " , self.direction
		print "Speed: " , self.speed		

myCar = Car("001" , "Herbie" , 0, 10)
myCar.carStatus()

action = ""

while action != "XXX":
	print "Drive your Car"
	print "+ to accelerate"
	print "- to brake"
	print "l to turn left"
	print "r to turn right"
	action = raw_input("What would you like to do (XXX to exit):")
	
	if action == "+":
		myCar.accelerate()
	elif action == "-":
		myCar.brake()
	elif action == "l":
		myCar.turnLeft()
	elif action == "r":
		myCar.turnRight()
	else:
		print "Action not recognized"
	myCar.carStatus()




