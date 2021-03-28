import time
sen1 = []
sen2 = []
sen3 = []
RPM = 6
m1 = "HIGH"     # Connected to the +ve motor pin! (defined in .txt file)
m2 = "LOW"      # Connected to the -ve motor pin! (defined in .txt file)

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
		if m1 == "HIGH" and m2 == "LOW": print("Moving Anticlockwise!")
		elif m1 == "LOW" and m2 == "HIGH": print("Running Clockwise!")
		else: print("Is not moving!")
		
	def calibrate(self):
		flag = 0
		last = 0
		m1 = "HIGH"
		m2 = "LOW"
		# i = 0											# comment
		# s1 = 1000										# comment
		while len(sen1) <= 360:
			s1 = 0       	# analogRead(sensor_1)		# uncomment
			s2 = 0     		# analogRead(sensor_2)
			s3 = 0    		# analogRead(sensor_3)
			# s1 -= 1									# comment
			if flag == 0 and s1 > last and s1 == 980:
				flag = 1
				print("Started Recording!")
			if flag == 1:
				sen1.append(s1)
				sen2.append(s2)
				sen3.append(s3)
				# print("\nAt " + str(i) + " degree sensor 1 = " + str(s1) + ", sensor 2 = " + str(s2) + ", sensor 3 = " + str(s3) +".")
				# i+=1
				last = s1
				wait = 500/(3*RPM)
				time.sleep(wait/1000)
		print("Recorded!")
		m1 = "LOW"
		m2 = "LOW"

FrontLeft = motor("FL")
FrontLeft.calibrate()
