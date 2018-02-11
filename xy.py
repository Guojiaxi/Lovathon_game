import math

#circle coordinates
# radius = 10;
# for angle in range(0, 361):
# 	theta = math.radians(angle)
# 	x = radius*math.cos(theta)
# 	y = radius*math.sin(theta)
# 	print repr(x) + ',' + repr(y)



#zigzag coordinates
#z is how long the map is
# def zigzag(x,y,z):
# 	x = 0
# 	y = 0
# 	while (x < z):
# 		if (y == 0):
# 			for i in range (0,5):
# 				y += 1
# 				x += 1
# 				print repr(x) + ',' + repr(y)

# 		if (y == 5):
# 			for i in range (0,5):
# 				y -= 1
# 				x += 1
# 				print repr(x) + ',' + repr(y)
		

#linear coordinates
def line(x,y,z):
	x = 0
	ycoordinate = y 
	while (x < z):
		x += 1
		print repr(x) + ',' + repr(ycoordinate)
c=0
d=10
e=20

line(c,d,e)