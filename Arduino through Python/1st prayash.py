
from pyfirmata import Arduino, util
import time
board = Arduino('/dev/ttyACM0')
board.digital[13].write(1)
it = util.Iterator(board)
it.start()
while True:
	time.sleep()
	board.analog[3].enable_reporting()
	test=board.analog[3].read()
	print(test)
