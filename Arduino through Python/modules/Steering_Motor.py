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

# Defining Motor Pins:- 
# "mp" denotes "motor pins",
# "ms" denotes "motor pin state(0/1)"
msfl1 = 0
msfl2 = 0

msfr1 = 0
msfr2 = 0

msbl1 = 0
msbl2 = 0

msbr1 = 0
msbr2 = 0
	
# Store Calibration Info In Lists
senfl1 = []
senfl2 = []
senfl3 = []

senfr1 = []
senfr2 = []
senfr3 = []

senbl1 = []
senbl2 = []
senbl3 = []

senbr1 = []
senbr2 = []
senbr3 = []

RPMfl = 6
RPMfr = 6
RPMbl = 6
RPMbr = 6

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

	def status(self, ID):
		'''Method to know the state of the motor!'''
		if ID == "fl": 
			ms1 = msfl1
			ms2 = msfl2
		if ID == "fr":
			ms1 = msfr1
			ms2 = msfr2
		if ID == "bl":
			ms1 = msbl1
			ms2 = msbl2
		if ID == "br":
			ms1 = msbr1
			ms2 = msbr2
		if ms1 == 1 and ms2 == 0: print(ID + " Motor is Moving Anticlockwise!")
		elif ms1 == 0 and ms2 == 1: print(ID + " Motor is Moving Clockwise!")
		else: print(ID + " Motor is NOT moving!")

	def calibrate(self, ID): # Please do not read the commented out lines, you would mislead youself!
		'''Method to calibrate the motors'''
		calpt = self.calpt
		flag = 0
		last = 0
		if ID == "fl":
			mp1 = 12
			mp2 = 11
			sp1 = "A0"
			sp2 = "A1"
			sp3 = "A2"
		if ID == "fr":
			mp1 = 10
			mp2 = 9
			sp1 = "A3"
			sp2 = "A4"
			sp3 = "A5"
		if ID == "bl":
			mp1 = 8
			mp2 = 7
			sp1 = "A0"
			sp2 = "A1"
			sp3 = "A2"
		if ID == "br":
			mp1 = 6
			mp2 = 5
			sp1 = "A3"
			sp2 = "A4"
			sp3 = "A5"
			
		if ID == "fl" or ID == "fr":
			boardf.digital[mp1].write(1)
			if ID == "fl": msfl1 = 1
			if ID == "fr": msfr1 = 1
		if ID == "bl" or ID == "br":
			boardb.digital[mp1].write(1)
			if ID == "bl": msbl1 = 1
			if ID == "br": msbr1 = 1
			
		if ID == "fl" or ID == "fr":
			boardf.digital[mp2].write(0)
			if ID == "fl": msfl2 = 0
			if ID == "fr": msfr2 = 0
		if ID == "bl" or ID == "br":
			boardb.digital[mp2].write(1)
			if ID == "bl": msbl2 = 0
			if ID == "br": msbr2 = 0
			
		while len(sen1) <= 360:
			if ID == "fl" or ID == "fr":
				s1 = boardf.analog[sp1].read()
				s2 = boardf.analog[sp2].read()
				s3 = boardf.analog[sp3].read()
			if ID == "bl" or ID == "br":
				s1 = boardb.analog[sp1].read()
				s2 = boardb.analog[sp2].read()
				s3 = boardb.analog[sp3].read()
			if flag == 0 and s1 > last and s1 == calpt:
				flag = 1
				print("Started Recording!")
			if flag == 1:
				if ID == "fl":
					senfl1.append(s1)
					senfl2.append(s2)
					senfl3.append(s3)
				if ID == "fr":
					senfr1.append(s1)
					senfr2.append(s2)
					senfr3.append(s3)
				if ID == "bl":
					senbl1.append(s1)
					senbl2.append(s2)
					senbl3.append(s3)
				if ID == "br":
					senbr1.append(s1)
					senbr2.append(s2)
					senbr3.append(s3)
				# print("\nAt " + str(sen1.index(s1)) + " degree sensor 1 = " + str(s1) + ", sensor 2 = " + str(s2) + ", sensor 3 = " + str(s3) +".")
				last = s1
				if ID == "fl": RPM = RPMfl
				if ID == "fr": RPM = RPMfr
				if ID == "bl": RPM = RPMbl
				if ID == "br": RPM = RPMbr
				wait = 500/(3*RPM)
				time.sleep(wait/1000)
		print("Recorded!")
		if ID == "fl" or ID == "fr":
			boardf.digital[mp1].write(0)
			if ID == "fl": msfl1 = 0
			if ID == "fr": msfr1 = 0
		if ID == "bl" or ID == "br":
			boardb.digital[mp1].write(1)
			if ID == "bl": msbl1 = 0
			if ID == "br": msbr1 = 0
			
		if ID == "fl" or ID == "fr":
			boardf.digital[mp2].write(0)
			if ID == "fl": msfl2 = 0
			if ID == "fr": msfr2 = 0
		if ID == "bl" or ID == "br":
			boardb.digital[mp2].write(1)
			if ID == "bl": msbl2 = 0
			if ID == "br": msbr2 = 0

	def current_position(self, ID):
		'''Method to know the current position of the wheel!'''
		if ID == "fl" or ID == "fr":
			s1 = boardf.analog[sp1].read()
			s2 = boardf.analog[sp2].read()
			s3 = boardf.analog[sp3].read()
		if ID == "bl" or ID == "br":
			s1 = boardb.analog[sp1].read()
			s2 = boardb.analog[sp2].read()
			s3 = boardb.analog[sp3].read()
		for i in range(360):
			if s1 > (sen1[i]-2) and s1 < (sen1[i]+2):
				if s2 > (sen2[i]-2) and s2 < (sen2[i]+2):
					if s3 > (sen3[i]-2) and s3 < (sen3[i]+2):
						# print("Position of the wheel is " + str(i) + " degree!")
						return i
						break

def SMgoto(ID, f):			# "f" denotes final position
	'''Function to take the wheel to a specific position'''
	ID = Steering_Motor(ID)	
	for i in range(3):
		i = ID.current_position()
		if f < i:
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(1)
				if ID == "fl": msfl1 = 1
				if ID == "fr": msfr1 = 1
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 1
				if ID == "br": msbr1 = 1
				
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(0)
				if ID == "fl": msfl2 = 0
				if ID == "fr": msfr2 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 0
				if ID == "br": msbr2 = 0
				
			if ID == "fl": RPM = RPMfl
			if ID == "fr": RPM = RPMfr
			if ID == "bl": RPM = RPMbl
			if ID == "br": RPM = RPMbr					
			time.sleep((500*(i-f))/(3*RPM))
			
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(0)
				if ID == "fl": msfl1 = 0
				if ID == "fr": msfr1 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 0
				if ID == "br": msbr1 = 0
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(0)
				if ID == "fl": msfl2 = 0
				if ID == "fr": msfr2 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 0
				if ID == "br": msbr2 = 0	
		if f > i:
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(1)
				if ID == "fl": msfl2 = 1
				if ID == "fr": msfr2 = 1
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 1
				if ID == "br": msbr2 = 1
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(0)
				if ID == "fl": msfl1 = 0
				if ID == "fr": msfr1 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 0
				if ID == "br": msbr1 = 0
				
			if ID == "fl": RPM = RPMfl
			if ID == "fr": RPM = RPMfr
			if ID == "bl": RPM = RPMbl
			if ID == "br": RPM = RPMbr			
			time.sleep((500*(f-i))/(3*RPM))
			
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(0)
				if ID == "fl": msfl1 = 0
				if ID == "fr": msfr1 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 0
				if ID == "br": msbr1 = 0
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(0)
				if ID == "fl": msfl2 = 0
				if ID == "fr": msfr2 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 0
				if ID == "br": msbr2 = 0
		
def SMmove(ID, angle, direction):	# Direction takes 2 values, "c" and "ac"!
	'''Function to move the wheel in some specific
	direction, for some some specific angle!
	'''	
	ID = Steering_Motor(ID)	
	for i in range(3):
		if direction == "c":
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(1)
				if ID == "fl": msfl1 = 1
				if ID == "fr": msfr1 = 1
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 1
				if ID == "br": msbr1 = 1
				
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(0)
				if ID == "fl": msfl2 = 0
				if ID == "fr": msfr2 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 0
				if ID == "br": msbr2 = 0
			
			if ID == "fl": RPM = RPMfl
			if ID == "fr": RPM = RPMfr
			if ID == "bl": RPM = RPMbl
			if ID == "br": RPM = RPMbr	
			time.sleep((500*angle)/(3*RPM))
			
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(0)
				if ID == "fl": msfl1 = 0
				if ID == "fr": msfr1 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 0
				if ID == "br": msbr1 = 0
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(0)
				if ID == "fl": msfl2 = 0
				if ID == "fr": msfr2 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 0
				if ID == "br": msbr2 = 0
		if direction == "ac":
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(1)
				if ID == "fl": msfl2 = 1
				if ID == "fr": msfr2 = 1
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 1
				if ID == "br": msbr2 = 1
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(0)
				if ID == "fl": msfl1 = 0
				if ID == "fr": msfr1 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 0
				if ID == "br": msbr1 = 0
			
			if ID == "fl": RPM = RPMfl
			if ID == "fr": RPM = RPMfr
			if ID == "bl": RPM = RPMbl
			if ID == "br": RPM = RPMbr		
			time.sleep((500*angle)/(3*RPM))
			
			if ID == "fl" or ID == "fr":
				boardf.digital[mp1].write(0)
				if ID == "fl": msfl1 = 0
				if ID == "fr": msfr1 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp1].write(1)
				if ID == "bl": msbl1 = 0
				if ID == "br": msbr1 = 0
			if ID == "fl" or ID == "fr":
				boardf.digital[mp2].write(0)
				if ID == "fl": msfl2 = 0
				if ID == "fr": msfr2 = 0
			if ID == "bl" or ID == "br":
				boardb.digital[mp2].write(1)
				if ID == "bl": msbl2 = 0
				if ID == "br": msbr2 = 0
			
# fl = Steering_Motor("fl")
# fl.status()
# fl.calibrate()
# fl.status()
