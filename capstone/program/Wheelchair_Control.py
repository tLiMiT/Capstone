# Wheelchair_Control.py
#
#

import sys
import time
import signal
import serial

import Configuration as configuration

from PyQt4 import QtCore

#####################################################################
# Globals
#####################################################################

DEBUG = 1

DEFAULT_COMMAND = 'console'
DEFAULT_SERIAL_DEVICE = '/dev/ttyACM0'

DEFAULT_WHEELCHAIR_SPEED = 1
DEFAULT_WHEELCHAIR_COMMAND = 'stop'

ARDUINO_INITIALIZATION_TIME = 2
COMMAND_CHARACTER = 'x'
GUI_SLEEP_TIMER = 1 * 100 # 100ms

# need to fill in speed data that goes to the wheelchair
WHEELCHAIR_COMMANDS = {
    1: { # speed 1
        'forward':  '00000000',
        'reverse':  '00000000',
        'left':     '00000000',
        'right':    '00000000',
        'stop':     '00000000',
    },
    2: { # speed 2
        'forward':  '00000000',
        'reverse':  '00000000',
        'left':     '00000000',
        'right':    '00000000',
        'stop':     '00000000',
    },
    3: { # speed 3
        'forward':  '00000000',
        'reverse':  '00000000',
        'left':     '00000000',
        'right':    '00000000',
        'stop':     '00000000',
    },
}

DRIVE_CONTROLS = {
    'fwd':      (1<<1, 1<<0),
    'rev':      (1<<3, 1<<2),
    'right':    (1<<5, 1<<4),
    'left':     (1<<7, 1<<6),
}

MOVE_COMANDS ={
    # might change this to WASD for 1337 skillz
    ' ' : 'stop',
    'w' : 'fwd',
    's' : 'rev',
    'a' : 'left',
    'd' : 'right',
		}

SPEED_COMMANDS = {
    '1' : 'speed-1',
    '2' : 'speed-2',
    '3' : 'speed-3',
}

STOP_TIME = 0
STOP_INTERVAL = 0.2
ALARM_INTERVAL = 0.1

#####################################################################
# Classes
#####################################################################

class capstone_program_wheelchair_control(QtCore.QThread):

    def __init__(self, \
                 device_address=DEFAULT_SERIAL_DEVICE, \
                 command=DEFAULT_COMMAND, \
                 DEBUG=DEBUG, \
                 parent=None):

        QtCore.QThread.__init__(self, parent)
        
        self.log = None
	self.DEBUG = DEBUG
	self.parent = parent
	
	self.device_address = device_address
	self.command = command
	
	self.wheelchair_speed = DEFAULT_WHEELCHAIR_SPEED
	self.wheelchair_command = DEFAULT_WHEELCHAIR_COMMAND
	
	self.device = None
	self.initializeSerial()
		
	self.keep_running = True

    #####################################################################

    def initializeSerial(self):

        # subject to change
        baudrate = 9600 
	bytesize = 8
	parity = 'NONE'
	stopbits = 1
	software_flow_control = 'f'
	rts_cts_flow_control = 't'
	timeout = 5
		
	# convert bytesize
	if (bytesize == 5):
            init_byte_size = serial.FIVEBITS
	elif (bytesize == 6):
            init_byte_size = serial.SIXBITS
	elif (bytesize == 7):
            init_byte_size = serial.SEVENBITS
	elif (bytesize == 8):
            init_byte_size = serial.EIGHTBITS
	else:
            init_byte_size = serial.EIGHTBITS
		
	# convert parity
	if (parity == 'NONE'):
            init_parity = serial.PARITY_NONE
	elif (parity == 'EVEN'):
            init_parity = serial.PARITY_EVEN
	elif (parity == 'ODD'):
            init_parity = serial.PARITY_ODD
	else:
            init_parity = serial.PARITY_NONE
		
	# convert stopbits
	if (stopbits == 1):
            init_stopbits = serial.STOPBITS_ONE
	elif (stopbits == 2):
            init_stopbits = serial.STOPBITS_TWO
	else:
            init_byte_size = serial.STOPBITS_ONE
		
	# convert software flow control
	if (software_flow_control == 't'):
            init_software_flow_control = 1
	else:
            init_software_flow_control = 0
		
	# convert rts cts flow control
	if (rts_cts_flow_control == 't'):
            init_rts_cts_flow_control = 1
	else:
            init_rts_cts_flow_control = 0
		
	self.device = serial.Serial(port = self.device_address, \
                                    baudrate = baudrate, \
                                    bytesize = init_byte_size, \
                                    parity = init_parity, \
                                    stopbits = init_stopbits, \
                                    xonxoff = init_software_flow_control, \
                                    rtscts = init_rts_cts_flow_control, \
                                    timeout = timeout)
		
		
	self.sendCommand(self.wheelchair_speed, self.wheelchair_command)
		
	time.sleep(ARDUINO_INITIALIZATION_TIME)

    #####################################################################

    def sendCommand(self, speed, command):

        output = '%s%s' % (COMMAND_CHARACTER, WHEELCHAIR_COMMANDS[speed][command])

	self.device.write(output)

	if self.DEBUG:
            print "--> Wheelchair Command: %s (Speed %i) [%s]" % (command, speed, output)

	self.wheelchair_speed = speed
	self.wheelchair_command = command

    #####################################################################

    def alarmHandler(self, arg1, arg2):
        print 'ALARM!'
        if STOP_TIME < time.time():
            self.stopBot()


    def initAlarm(self):
        signal.alarm(ALARM_INTERVAL)
        signal.signal(signal.SIGALRM, alarmHandler)


    def setOutput(self, data):
        output = data ^ int('00110011', 2)

        output = self.int2bin(output)
        self.device.write('x%s' % output)

        print 'Output set to: ', output
        # might change to WASD
        print 'commands to move: w, a, s, d, SPACE = stop, x = quit'


    def moveBot(self, dir, speed):
        output = 0
        pins = DRIVE_CONTROLS[dir]
        
        if speed == 1:
            output = pins[0]
        elif speed == 2:
            output = pins[1]
	elif speed == 3:
            output = pins[0] | pins[1]
            
        self.setOutput(output)
        time.sleep(STOP_INTERVAL)
        self.stopBot()


    def stopBot(self):
        self.setOutput(0)


    def int2bin(self, n, count=8):
        return "".join([str((n >> y) & 1) for y in range(count-1, -1, -1)])

    #####################################################################

    def consoleControl(self):

        if (sys.platform == 'win32'):
            if self.DEBUG:
                print "---> Wheelchair Control: Console mode unavailable under Windows"

            self.exitThread()

            MYGETCH = Getch()

            self.stopBot()

            speed = DEFAULT_WHEELCHAIR_SPEED

            while True:
                cmd = MYGETCH()
                if cmd == 'x':
                    exit()
                if cmd in SPEED_COMMANDS.keys():
                    speed = int(cmd)
                    print SPEED_COMMANDS[cmd]
		elif cmd in MOVE_COMANDS.keys():
                    if MOVE_COMANDS[cmd] == 'stop':
                        self.stopBot()
                    else:
                        print MOVE_COMANDS[cmd]
                        self.moveBot(MOVE_COMANDS[cmd], speed)
                        STOP_TIME = time.time() + STOP_INTERVAL

    #####################################################################

    def processCommand(self):

        if (self.command == 'console'):
            self.consoleControl()

    #####################################################################

    def run(self):

        if self.DEBUG:
            print "<---- [%s] Main thread running" % "Wheelchair Control"

	self.processCommand()

	self.exec_()

    #####################################################################

    def exitThread(self, callThreadQuit=True):

        try:
            self.device.stop()
        except:
            pass
        
        if callThreadQuit:
            QtCore.QThread.quit(self)

#####################################################################

class Getch:
    def __init__(self):
        import tty, sys
        
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

#####################################################################
# Main
#####################################################################

if __name__ == '__main__':

    # Perform correct KeyboardInterrupt handling
    signal.signal(signal.SIGINT, signal.SIG_DFL)

    # Collect default settings and command line parameters
    command = DEFAULT_COMMAND

    for each in sys.argv:
        if each.startswith("--device="):
            device = each[ len("--device="): ]
        elif each.startswith("--command="):
            command = each[ len("--command="): ]
            
    app = QtCore.QCoreApplication(sys.argv)
    wheelchair = capstone_program_wheelchair_control(device_address=device, \
                                                     command=command, \
                                                     DEBUG=DEBUG)
    wheelchair.start()

    sys.exit(app.exec_())
