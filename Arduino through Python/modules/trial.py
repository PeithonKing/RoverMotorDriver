'''
import time
eye = "brown"

class Dog():
	def __init__(self, name, age):
		self.name = name
		self.age = age
	
	def sit(self):
		print("The " + eye + " eyed dog is sitting now!")
	
	def stand(self):
		name = self.name
		print(name + ", the dog is standing now!")
		Dog.sit(self)

def st(nam):
	nam = Dog(nam, 5)
	nam.sit()
		
Jimmy = Dog("Jimmy", 5)
Jimmy.stand()

'''
while True:
	command = input("\nWhat should the Rover do?")
	try: leg, do = command.split(",")
	except:
		print("Invalid Input!1")
		continue
	leg = leg.strip().lower()
	do = do.strip().lower()
	
	legs = []
	if leg == "fl": legs.append("fl")
	elif leg == "fr": legs.append("fr")
	elif leg == "bl": legs.append("bl")
	elif leg == "br": legs.append("br")
	elif leg == "f":
		legs.append("fl")
		legs.append("fr")
	elif leg == "b":
		legs.append("bl")
		legs.append("br")
	elif leg == "l":
		legs.append("fl")
		legs.append("bl")
	elif leg == "r":
		legs.append("fr")
		legs.append("br")
	elif leg == "a":
		legs = ["fl", "fr", "bl", "br"]
	else:
		print("Invalid Input!2")
		continue
		
	if "status" in do: 
		for leg in legs:
			print("Status of " + leg + " is being shown!")
	elif "cal" in do:
		for leg in legs:
			print(leg + " is being calibrated!")
	elif "pos" in do:
		for leg in legs:
			print("Position of " + leg + " is being shown!")
	elif "move" in command:
		do = do.replace("move", "").strip()
		try:
			theta, direction = do.split(":")
			# print("theta = " + theta)
			# print("direction = " + direction)			
		except:
			print("Invalid Input!3")
			continue
		for leg in legs:
			print(leg + " is being moved through " + theta + " degree " + direction)
		
	elif "goto" in command:
		do = do.replace("goto", "").strip()
		for leg in legs:
			print(leg + " is being taken to " + do)
	else:
		print("Invalid Input!4")
		continue

