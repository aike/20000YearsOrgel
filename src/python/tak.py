#!/usr/bin/python

import time
import liblo
from LCD import LCD
from TSL2561 import TSL2561

saved_number = None
start_number = None
count = 0

def tak(x, y, z):
	global count
	count += 1
	lcd.lower_write(count)

	if count >= start_number:
		liblo.send(target, '/note', x, y, z)
		lcd.upper_write3(x, y, z)
		checkSensor()
		time.sleep(2)

	if x <= y:
		return y
	else:
		return tak(tak(x-1,y,z),tak(y-1,z,x),tak(z-1,x,y))


# Open/Close Box Check
def checkSensor():
	light = tsl.readData()
	print light
	while light < 20:
		suspend(count)
		time.sleep(1)
		light = tsl.readData()
		print light

# on Close Box
def suspend(number):
	global saved_number
	if number != saved_number:
		f = open ('datafile.txt', 'w')
		f.write(str(number))
		saved_number = number
		f.close()

# on PowerON
def resume():
	num = 0
	try:
		f = open ('datafile.txt', 'r')
		num = int(f.read())
		f.close()
	except:
		num = 0
	return num


tsl = TSL2561()
lcd = LCD()
start_number = resume()
target = liblo.Address('127.0.0.1', 12000)
tak(17,10,0)

