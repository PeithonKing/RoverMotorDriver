import pyfirmata as pf
board = pf.Arduino("COM3")
it = pf.util.Iterator(board)
it.start()
pin=A3

while True:
	reading = board.analog[pin].read()
	print(reading)
