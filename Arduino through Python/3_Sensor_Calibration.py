import pyfirmata as pf
import time
board = pf.Arduino("COM3")
it = pf.util.Iterator(board)
it.start()

# Defining Motor Pins:- "mp" denotes "motor pins",
# "ms" (see line 24 and 25) denotes "motor pin state (high/low)"
mp1 = 11
mp2 = 10

# Sensor Pins
# s1, s2 and s3 are used to store the values read from the respective pins!
sp1=A1
sp2=A2
sp3=A3

# Store Calibration Info In Lists
sen1 = []
sen2 = []
sen3 = []

RPM = 6
ms1 = 0					# make it high to rotate anticlockwise(+ve)
ms2 = 0

def pinhi(pin): 		# function to make a pin HIGH
	board.digital[pin].write(1)
	if pin == mp1: ms1 = 1
	if pin == mp2: ms2 = 1

def pinlo(pin): 		# function to make a pin LOW
	board.digital[pin].write(0)
	if pin == mp1: ms1 = 0
	if pin == mp2: ms2 = 0

class Steering_Motor():
	'''Defining general properties of steering motors!
	We are assuming that the sensors are parts of the motors!'''

	def __init__(self, ID, calpt):
		'''
		ID is to define which leg we are talking about!
		ID consists of 2 letters:-
		ID letter 1 :- F = Front, B = Back
		ID letter 2 :- L = Left, R = Right
		
		"calpt" is the value of the sensor 1,
		when the wheel is @ zero degrees
		as described in calibration file!
		'''
		self.ID = ID
		self.calpt = calpt

	def status(self):
		'''Method to know the state of the motor!'''
		if ms1 == 1 and ms2 == 0: print("Moving Anticlockwise!")
		elif ms1 == 0 and ms2 == 1: print("Moving Clockwise!")
		else: print("Is not moving!")

	def calibrate(self): # Please do not read the commented out lines, you would mislead youself!
		'''Method to calibrate the motors'''
		calpt = self.calpt
		flag = 0
		last = 0
		pinhi(mp1)
		pinlo(mp2)
		# i = 0											# comment
		# s1 = 1000										# comment
		while len(sen1) <= 360:
			s1 = board.analog[sp1].read()       		# uncomment
			s2 = board.analog[sp2].read()
			s3 = board.analog[sp3].read()
			# s1 -= 1									# comment
			if flag == 0 and s1 > last and s1 == calpt:
				flag = 1
				print("Started Recording!")
			if flag == 1:
				sen1.append(s1)
				sen2.append(s2)
				sen3.append(s3)
				print("\nAt " + str(i) + " degree sensor 1 = " + str(s1) + ", sensor 2 = " + str(s2) + ", sensor 3 = " + str(s3) +".")  # comment
				# i+=1									# comment
				last = s1
				wait = 500/(3*RPM)
				time.sleep(wait/1000)					# uncomment
		print("Recorded!")
		pinlo(mp1)
		pinlo(mp2)

	def current_position(self):
		'''Method to know the current position of the wheel!'''
		s1 = board.analog[sp1].read()
		s2 = board.analog[sp2].read()
		s3 = board.analog[sp3].read()

		for i in range(360):
			if s1 > (sen1[i]-2) and s1 < (sen1[i]+2):
				if s2 > (sen2[i]-2) and s2 < (sen2[i]+2):
					if s3 > (sen3[i]-2) and s3 < (sen3[i]+2):
						# print("Position of the wheel is " + str(i) + " degree!")
						return i
						break

def goto(name, f):			# "f" denotes final position
	'''Function to take the wheel to a specific position'''
	name = Steering_Motor(name)	
	for i in range(3):
		i = name.current_position()
		if f < i:
			pinhi(mp1)
			pinlo(mp2)		
			time.sleep((500*(i-f))/(3*RPM))
			pinlo(mp1)
			pinlo(mp2)	
		if f > i:
			pinhi(mp2)
			pinlo(mp1)		
			time.sleep((500*(f-i))/(3*RPM))
			pinlo(mp1)
			pinlo(mp2)
		
def move(name, angle, direction):	# Direction takes 2 values, "+" and "-"!
	'''Function to move the wheel in some specific
	direction, for some some specific angle!
	'''	
	name = Steering_Motor(name)	
	for i in range(3):
		i = name.current_position()
		if direction = "+":
			pinhi(mp1)
			pinlo(mp2)		
			time.sleep((500*angle)/(3*RPM))
			pinlo(mp1)
			pinlo(mp2)	
		if direction = "-":
			pinhi(mp2)
			pinlo(mp1)		
			time.sleep((500*angle)/(3*RPM))
			pinlo(mp1)
			pinlo(mp2)

# FrontLeft = Steering_Motor("FL")
# FrontLeft.status()
# FrontLeft.calibrate()
# FrontLeft.status()
