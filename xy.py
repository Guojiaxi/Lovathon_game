import math
from globalvars import *

# #circle coordinates
# def circular(x,y,r):
# 	radius = 10
# 	for angle in range(0, 361):
# 		theta = math.radians(angle)
# 		x = radius*math.cos(theta)
# 		y = radius*math.sin(theta)

def figure_eight(t):
	a = 150
	return (a*math.cos(t)+(width/2), a*math.sin(2*t)+(height/2))

# #zigzag coordinates
# #z is how long the map is
# def zigzag(x,y,z):
# 	x = 0
# 	y = 0
# 	while (x < z):
# 		if (y == 0):
# 			for i in range (0,5):
# 				y += 1
# 				x += 1
#
# 		if (y == 5):
# 			for i in range (0,5):
# 				y -= 1
# 				x += 1
#
#
# #linear coordinates
# def line(x,y,z):
# 	x = 0
# 	ycoordinate = y
# 	while (x < z):
# 		x += 1
