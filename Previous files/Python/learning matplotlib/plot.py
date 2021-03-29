import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use("fivethirtyeight")

fig = plt.figure()
axl = fig.add_subplot(1, 1, 1)

def animate(i):
	graph_data = open("example.txt", "r").read()
	lines = graph_data.split("\n")
	xs = []
	ys = []
	for line in lines:
		if len(line) > 1:
			x,y = line.split(",")
			xs.append(x)
			ys.append(y)
	axl.clear()
	axl.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.show()
