from serial import Serial
ser = Serial(39)         # open first serial port
print ser.name          # check which port was really used
new_ser.write('W')      # write a string
s = ser.read(10)        # read up to ten bytes (timeout)
line = ser.readline()   # read a '\n' terminated line
ser.close()            # close port
