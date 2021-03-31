def motor_pins(ID):
	if ID == "fl":
		mp1 = 12
		mp2 = 11
	if ID == "fr":
		mp1 = 10
		mp2 = 9
	if ID == "bl":
		mp1 = 8
		mp2 = 7
	if ID == "br":
		mp1 = 6
		mp2 = 5


mp1 = 54
mp2 = 25
print("mp1 = " + str(mp1) + "   mp2 = " + str(mp2))
motor_pins("fl")
print("mp1 = " + str(mp1) + "   mp2 = " + str(mp2))
