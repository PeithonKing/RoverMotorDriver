import pyfirmata as pf
import time
board = pf.Arduino("COM3")
it = pf.util.Iterator(board)
it.start()

# Defining Motor Pins:- "mp" denotes "motor pins"
# "ms" (see line 22 and 23) denotes "motor pin state (high/low)"
mp1 = 11
mp2 = 10

# Sensor Pins
sp1=A1
sp2=A2
sp3=A3

# Store Calibration Info In Lists
sen1 = []
sen2 = []
sen3 = []

RPM = 6
ms1 = 1
ms1 = 0

def pinhi(pin):
	board.digital[pin].write(1)
	if pin == mp1: ms1 = 1
	if pin == mp2: ms2 = 1

def pinlo(pin):
	board.digital[pin].write(0)
	if pin == mp1: ms1 = 0
	if pin == mp2: ms2 = 0

class motor():
	'''Defining general properties of steering motors!
	We are assuming that the sensors are parts of the motors!'''
		
	def __init__(self, ID): 
		'''ID is to define which leg we are talking about!
		ID consists of 2 letters:-
		ID letter 1 :- F = Front, B = Back
		ID letter 2 :- L = Left, R = Right'''
		self.ID = ID
	
		
	def status(self):
		if ms1 == 1 and ms2 == 0: print("Moving Anticlockwise!")
		elif ms1 == 0 and ms2 == 1: print("Running Clockwise!")
		else: print("Is not moving!")
		
	def calibrate(self):
		flag = 0
		last = 0
		pinhi(mp1)
		pinlo(mp2)
		i = 0											# comment
		s1 = 1000										# comment
		while len(sen1) <= 360:
			# s1 = 0       	# analogRead(sensor_1)		# uncomment
			s2 = 0     		# analogRead(sensor_2)
			s3 = 0    		# analogRead(sensor_3)
			s1 -= 1										# comment
			if flag == 0 and s1 > last and s1 == 550:
				flag = 1
				print("Started Recording!")
			if flag == 1:
				sen1.append(s1)
				sen2.append(s2)
				sen3.append(s3)
				print("\nAt " + str(i) + " degree sensor 1 = " + str(s1) + ", sensor 2 = " + str(s2) + ", sensor 3 = " + str(s3) +".")
				i+=1									# comment
				last = s1
				wait = 500/(3*RPM)
				# time.sleep(wait/1000)					# uncomment
		print("Recorded!")
		pinlo(mp1)
		pinlo(mp2)

FrontLeft = motor("FL")
FrontLeft.status()
FrontLeft.calibrate()
FrontLeft.status()
print("m1 = " + m1)
print("m2 = " + m2)
