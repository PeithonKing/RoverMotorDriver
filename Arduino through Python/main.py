from modules.Steering_Motor import *
from pyfirmata import Arduino, util
import time
portf = "/dev/ttyACM0"
portb = "/dev/ttyACM1"
boardf = Arduino(portf)
boardb = Arduino(portb)
itf = util.Iterator(boardf)
itb = util.Iterator(boardb)
itf.start()
itb.start()

boardf.analog[A0].enable_reporting()
boardf.analog[A1].enable_reporting()
boardf.analog[A2].enable_reporting()
boardf.analog[A3].enable_reporting()
boardf.analog[A4].enable_reporting()
boardf.analog[A5].enable_reporting()

boardb.analog[A0].enable_reporting()
boardb.analog[A1].enable_reporting()
boardb.analog[A2].enable_reporting()
boardb.analog[A3].enable_reporting()
boardb.analog[A4].enable_reporting()
boardb.analog[A5].enable_reporting()


calptfl = 550
calptfr = 550
calptbl = 550
calptbr = 550

def start(ID, calpt):
	ID = Steering_Motor(ID, calpt)

start(fl, calptfl)			# Have the value of "calpt" and put here
start(fr, calptfr)
start(bl, calptbl)
start(br, calptbr)

RPMfl = 6			# RPM for front Front Left leg
RPMfr = 6			# RPM for front Front Right leg
RPMbl = 6			# RPM for front Back Left leg
RPMbr = 6			# RPM for front Back Right leg


while True:
	command = input("\nWhat should the Rover do?")
	try: leg, do = command.split(",")
	except:
		print("Invalid Input! 1")
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
		print("Invalid Input! 2")
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
			print("Invalid Input! 3")
			continue
		for leg in legs:
			SMmove(leg, int(theta), direction)
		
	if "goto" in command:
		do = do.replace("goto", "").strip()
		for leg in legs:
			SMgoto(leg, int(do))
	else:
		print("Invalid Input! 4")
		continue
