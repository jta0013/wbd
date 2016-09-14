#Joshua Ando 
#Testing
from Navigation.prod.Angle import Angle

angle1 = Angle()
angle2 = Angle()

angle1.setDegreesAndMinutes("45d0")
angle2.setDegreesAndMinutes("340d30")
angle1.add(angle2)

if angle1.degree == "25.5": 
    print"Addition Test Successful"
else: 
    print"Addition Test Fail"

angle1.setDegreesAndMinutes("0d0")
angle2.setDegreesAndMinutes("25d30")
angle1.subtract(angle2)
if angle1.degree == 334.5:
    print "Subtract Test Successful"
else: 
    print "Subtract Test Fail"

angle1.setDegrees(45.0)
angle2.setDegrees(45.1)
if angle1.compare(angle2) == -1: 
    print "Compare Test Successful"
else:
    print "Compare Test Fail"

angle1.getDegrees() 
print "getDegrees success"
angle1.getString()
print "getString success"



