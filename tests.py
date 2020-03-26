import model

m = model.Model()

print("Default model : {}".format(m))

print("\n ##### Test DK function #####")

print("Same speed")
m.m1.speed = 1
m.m2.speed = 1
print ("Model 1: {}".format(m))
linear_speed, rotation_speed = m.dk()
print("lin_speed={} rot_speed={}".format(linear_speed, rotation_speed))
if linear_speed == 1 and rotation_speed == 0:
    print("OK")
else :
    print("KO")

print("oposed speed")
m.m1.speed = 1
m.m2.speed = -1
print ("Model 2: {}".format(m))
linear_speed, rotation_speed = m.dk()
print("lin_speed={} rot_speed={}".format(linear_speed, rotation_speed))
if linear_speed == 0 and rotation_speed == 16.666666666666668: 
    print("OK")
else :
    print("KO")

print("1 motor speed")
m.m1.speed = 1
m.m2.speed = 0
print ("Model 3: {}".format(m))
linear_speed, rotation_speed = m.dk()
print("lin_speed={} rot_speed={}".format(linear_speed, rotation_speed))
if linear_speed == (m.m1.speed / 2) and rotation_speed == (m.m1.speed / 0.120):
    print("OK")
else :
    print("KO")

print("\n ##### Test IK function ##### ")
print("linear mouvement")
print ("Model 4: {}".format(m))
m.m1.speed, m.m2.speed = m.ik(1,0)
print("m1_speed={} m2_speed={}".format(m.m1.speed, m.m2.speed))
if m.m1.speed == 1 and m.m2.speed == 1:
    print("OK")
else :
    print("KO")

print("linear mouvement + rot")
print ("Model 5: {}".format(m))
m.m1.speed, m.m2.speed = m.ik(1,1)
print("m1_speed={} m2_speed={}".format(m.m1.speed, m.m2.speed))
if m.m1.speed == 1.06 and m.m2.speed == 0.94:
    print("OK")
else :
    print("KO")

print("rotatinal mouvement")
print ("Model 6: {}".format(m))
m.m1.speed, m.m2.speed = m.ik(0,1)
print("m1_speed={} m2_speed={}".format(m.m1.speed, m.m2.speed))
if m.m1.speed == 0.06 and m.m2.speed == -0.06:
    print("OK")
else :
    print("KO")

print("\n ##### Test Update function ##### ")


import model

m = model.Model()

print("Default model : {}".format(m))

print("\n ##### Test DK function #####")

print("Same speed")
m.m1.speed = 1
m.m2.speed = 1
print ("Model 1: {}".format(m))
linear_speed, rotation_speed = m.dk()
print("lin_speed={} rot_speed={}".format(linear_speed, rotation_speed))
if linear_speed == 1 and rotation_speed == 0:
    print("OK")
else :
    print("KO")

print("oposed speed")
m.m1.speed = 1
m.m2.speed = -1
print ("Model 2: {}".format(m))
linear_speed, rotation_speed = m.dk()
print("lin_speed={} rot_speed={}".format(linear_speed, rotation_speed))
if linear_speed == 0 and rotation_speed == 16.666666666666668: 
    print("OK")
else :
    print("KO")

print("1 motor speed")
m.m1.speed = 1
m.m2.speed = 0
print ("Model 3: {}".format(m))
linear_speed, rotation_speed = m.dk()
print("lin_speed={} rot_speed={}".format(linear_speed, rotation_speed))
if linear_speed == (m.m1.speed / 2) and rotation_speed == (m.m1.speed / 0.120):
    print("OK")
else :
    print("KO")

print("\n ##### Test IK function ##### ")
print("linear mouvement")
print ("Model 4: {}".format(m))
m.m1.speed, m.m2.speed = m.ik(1,0)
print("m1_speed={} m2_speed={}".format(m.m1.speed, m.m2.speed))
if m.m1.speed == 1 and m.m2.speed == 1:
    print("OK")
else :
    print("KO")

print("linear mouvement + rot")
print ("Model 5: {}".format(m))
m.m1.speed, m.m2.speed = m.ik(1,1)
print("m1_speed={} m2_speed={}".format(m.m1.speed, m.m2.speed))
if m.m1.speed == 1.06 and m.m2.speed == 0.94:
    print("OK")
else :
    print("KO")

print("rotatinal mouvement")
print ("Model 6: {}".format(m))
m.m1.speed, m.m2.speed = m.ik(0,1)
print("m1_speed={} m2_speed={}".format(m.m1.speed, m.m2.speed))
if m.m1.speed == 0.06 and m.m2.speed == -0.06:
    print("OK")
else :
    print("KO")

print("\n ##### Test Update function ##### ")


