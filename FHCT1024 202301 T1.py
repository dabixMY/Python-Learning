def test1202301Q1():

    #import math
    from math import sin, radians

    #INPUT velocity, angle
    velocity = float(input("Enter velocity                >> "))
    angle = float(input("Enter angle (0 to 90 degrees) >> "))

    gravity = 9.8
    maxHt = ((velocity**2)/(2*gravity))*((sin(radians(angle)))**2)

    print("Maximum height of the projectile is computed as {:.4f}".format(maxHt))

test1202301Q1()
#function name cannot begin with digit

