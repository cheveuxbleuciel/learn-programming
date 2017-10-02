import math

r = float(input())
area = math.pi * r**2
circum = 2 * math.pi * r

print("{0:.6f}".format(area), "{0:.6f}".format(circum))
