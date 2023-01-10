from adafruit_servokit import ServoKit
kit = ServoKit(channels=16)

while True:
	angle = int(input("winkel angeben: "))
	kit.servo[0].angle=angle
