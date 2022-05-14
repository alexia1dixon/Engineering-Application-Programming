import serial
from serial import Serial

# cc3220sf = serial.Serial('COM4', 115200) #(port number, baudrate) - create a serial object
with serial.Serial('COM4', 115200, timeout=10) as cc3220sf:
  line = cc3220sf.readlines()

print(line)