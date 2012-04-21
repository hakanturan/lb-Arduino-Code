# GPSDlWaypts.py
# Download waypoints to the GPS

# import time
# import serial
import string
 
# Configure the serial port to talk to the Arduino
# connection = serial.Serial('/dev/ttyACM0', 9600)

# read from the Arduino until receiving <DL> string
# data = connection.readline().strip('\n')
#while data <> "<DL>"
	# data = connection.readline().strip('\n')

# open the file for reading
fo = open("geocaching.loc", "r") 
line = fo.readline()
while line:
	line = fo.readline().strip('\n')
	#if the line starts with <coord then pull out the numbers
	# example: <coord lat="40.005717" lon="-79.598867"/>
	#send the numbers to the arduino
	if line[0:5] == "<coor":
		startPos = string.find(line, '\"') + 1
		endPos = string.find(line, '\"', startPos+1)
		startPos2 = string.find(line, '\"', endPos+1) + 1
		endPos2 = string.find(line, '\"', startPos2+1)
		print line[startPos:endPos] + "," + line[startPos2:endPos2]

# Close opened file 
fo.close()