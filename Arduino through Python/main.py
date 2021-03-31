'''
from modules.trial import *
Jimmy = Dog("Jimmy", 5)
Jimmy.stand()
# time.sleep(5)
st("Jimmy")
'''
from modules.Steering_Motor import *
import pyfirmata as pf
import time
portf = "COM3"
portb = "COM4"
boardf = pf.Arduino(portf)
boardb = pf.Arduino(portb)
itf = pf.util.Iterator(boardf)
itb = pf.util.Iterator(boardb)
itf.start()
itb.start()

def start(ID, calpt):
	ID = Steering_Motor(ID, calpt)

start(fl, calpt)			# Have the value of "calpt" and put here
start(fr, calpt)
start(bl, calpt)
start(br, calpt)


while True:
	command = input("\nWhat should the Rover do?")
	try: leg, do = command.split(",")
	except:
		print("Invalid Input!")
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
	else:
		print("Invalid Input!")
		continue
		
	if do == "status": 
		for leg in legs:
			leg.status(leg)
	if "cal" in do:
		for leg in legs:
			leg.calibrate(leg)
	if "pos" in do:
		for leg in legs:
			leg.current_position(leg)
	if "move" in command:
		do = do.replace("move", "").strip()
		try:
			theta, direction = do.split(":")
			# print("theta = " + theta)
			# print("direction = " + direction)			
		except:
			print("Invalid Input!3")
			continue
		for leg in legs:
			SMmove(leg, int(theta), direction)
		
	if "goto" in command:
		do = do.replace("goto", "").strip()
		for leg in legs:
			SMgoto(leg, int(do))
	else:
		print("Invalid Input!")
		continue
