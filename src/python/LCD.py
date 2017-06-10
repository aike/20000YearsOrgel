#!/usr/bin/python

import smbus
import time

class LCD:
	def __init__(self):
	    try:
		self.bus = smbus.SMBus(1)
		self.addr = 0x3e
		self.bus.write_i2c_block_data(self.addr, 0x00, [0x38, 0x39, 0x14, 0x78, 0x5f, 0x6a])
		time.sleep(0.3)
		self.bus.write_i2c_block_data(self.addr, 0x00, [0x0c, 0x01])
		time.sleep(0.3)
		self.bus.write_i2c_block_data(self.addr, 0x00, [0x06])
		time.sleep(0.3)
	    except IOError, err:
		return

	def upper_write(self, n):
	    try:
		s = str(n)
           	#     1234567890123456  
		s = ("                " + s)[-16:] 
		b = map(ord, list(s))
		self.bus.write_i2c_block_data(self.addr, 0x00, [0x80])
		self.bus.write_i2c_block_data(self.addr, 0x40, b)
	    except IOError, err:
		return

	def lower_write(self, n):
	    try:
        	s = str(n)
        	#     1234567890123456  
        	s = ("                " + s)[-16:] 
        	b = map(ord, list(s))
		self.bus.write_i2c_block_data(self.addr, 0x00, [0xc0])
		self.bus.write_i2c_block_data(self.addr, 0x40, b)
	    except IOError, err:
		return

	def upper_write3(self, n1, n2, n3):
	    try:
		s1 = str(n1)
		s2 = str(n2)
		s3 = str(n3)
           	#     12345  
		s1 = ("     " + s1)[-5:]
		s2 = ("     " + s2)[-5:]
		s3 = ("     " + s3)[-5:]
		s = " " + s1 + s2 + s3
		b = map(ord, list(s))
		self.bus.write_i2c_block_data(self.addr, 0x00, [0x80])
		self.bus.write_i2c_block_data(self.addr, 0x40, b)
	    except IOError, err:
		return


if __name__ == "__main__":
        lcd = LCD()
	lcd.lower_write(1234567890123456)
	n = 0
        while True:
		lcd.upper_write3(n, n+1, n+2)
		n += 1
		time.sleep(0.5)
