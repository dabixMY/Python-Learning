import math
import math as m
PI = m.pi
#PI = 22/7

#input & explicity converting the data type from string to float
mass= float(input("Enter mass >> "))
force= float(input("Enter force >> "))

period = 2*PI*math.sqrt(mass/(force*(1.005)**2))

print("Period of this simple pendulum is computed as {:.3f}".format(period)+".")
#print("Period of this simple pendulum is computed as %.3f."%period)


