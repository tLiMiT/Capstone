# GUI.py
#
#

import os, sys

if (sys.platform == 'win32'):
    DEFAULT_IMAGE_PATH = 'images'
    import _winreg as winreg
    import itertools
    import re
    import serial
else:
    # We're fucked, because we're not using Unix/Linux
    DEFAULT_IMAGE_PATH = 'images'

#import Configuration as configuration

from PyQt4 import QtCore, QtGui

from GUI_Design import Ui_Form as Design

#import Client as program_client
import Wheelchair_Control as wheelchair_control

import MessageSender as ms
import TextInserter as ti
import CharacterFreqLogger as cfl


# MAKE SURE TO CHANGE THIS FOR EACH COMPUTER
cfl.directory = 'C:\\Users\\Tim\\Documents\\GitHub\\Capstone\\capstone\\program\\'
#cfl.directory = 'C:\\Users\\C6\\Desktop\\bin\\'


#####################################################################
# GLOBALS
#####################################################################

DEBUG = 1

DEVICE_PATH = ''

MESSAGE_DESTINATION = ''
USER_MESSAGE = ''

RED = "background-color: rgb(255, 115, 80);"
BLUE = "background-color: rgb(112, 174, 255);"
BLANK = ""

CLICKS = 1
TYPING = False

BLUE_KEYS = {}
RED_KEYS = {}
IMPORTED_KEYS = {}

#####################################################################
# CLASSES
#####################################################################

class capstone_program_client_interface(QtGui.QWidget, Design):
    def __init__(self, log, server=None, DEBUG=DEBUG, parent=None):
        self.log = log
        self.DEBUG = DEBUG

        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        # map the buttons and callbacks
        self.configureSettings()
        self.connectWidgets()

        self.name = "Capstone Interface"
		
	# probably not needed
	#self.capstoneClient = None

	# set wheelchair
	self.wheelchair = None

	# set drive state	
	self.drive_state = 'stop_motors'
	self.current_speed = 0
	
        # add Becker's stuff
        temp = cfl.getCondFreq('', cfl.READWRITE_BINARY)
        self.selector = ti.ChoicePath(ti.huffmanAlgorithm(temp))

        # create a dictionary relating keyboard buttons to their respective characters
	self.keyboardDict = { \
            '1': self.keyboardNum1, \
            '2': self.keyboardNum2, \
            '3': self.keyboardNum3, \
            '4': self.keyboardNum4, \
            '5': self.keyboardNum5, \
            '6': self.keyboardNum6, \
            '7': self.keyboardNum7, \
            '8': self.keyboardNum8, \
            '9': self.keyboardNum9, \
            '0': self.keyboardNum0, \
            'A': self.keyboardA, \
            'B': self.keyboardB, \
            'C': self.keyboardC, \
            'D': self.keyboardD, \
            'E': self.keyboardE, \
            'F': self.keyboardF, \
            'G': self.keyboardG, \
            'H': self.keyboardH, \
            'I': self.keyboardI, \
            'J': self.keyboardJ, \
            'K': self.keyboardK, \
            'L': self.keyboardL, \
            'M': self.keyboardM, \
            'N': self.keyboardN, \
            'O': self.keyboardO, \
            'P': self.keyboardP, \
            'Q': self.keyboardQ, \
            'R': self.keyboardR, \
            'S': self.keyboardS, \
            'T': self.keyboardT, \
            'U': self.keyboardU, \
            'V': self.keyboardV, \
            'W': self.keyboardW, \
            'X': self.keyboardX, \
            'Y': self.keyboardY, \
            'Z': self.keyboardZ, \
            ',': self.keyboardComma, \
            '.': self.keyboardPeriod, \
            "'": self.keyboardApostrophe, \
            '?': self.keyboardQuestionMark, \
            '(': self.keyboardLeftParen, \
            ')': self.keyboardRightParen, \
            ':': self.keyboardColon, \
            ';': self.keyboardSemiColon, \
            '!': self.keyboardExclamationMark, \
            '/': self.keyboardSlash, \
            ' ': self.keyboardSpace, \
        }

        # initialize the keyboard keys as blue
	self.repaintKeys(self.keyboardDict.values(), BLUE)

    #####################################################################

    def configureSettings(self):

        ## Capstone Interface ##

        # Load the window icon
        image_path = "images/puzzlebox.ico"
	if not os.path.exists(image_path):
            image_path = os.path.join(DEFAULT_IMAGE_PATH, image_path)
		
	if os.path.exists(image_path):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(image_path), \
                           QtGui.QIcon.Normal, \
                           QtGui.QIcon.Off)
            self.setWindowIcon(icon)


        ## Wheelchair ##

        # Set status message
	self.labelWheelchairStatus.setText("Status: Disconnected")
	
	# Disable the drive controls
	self.pushButtonForward.setEnabled(False)
        self.pushButtonLeft.setEnabled(False)
	self.pushButtonRight.setEnabled(False)
	self.pushButtonReverse.setEnabled(False)
	self.pushButtonStop.setEnabled(False)

	
        ## Control Panel ##

	# Search for available Serial devices
	self.searchForDevices()

	
    #####################################################################

    def connectToWheelchair(self):
        
        # Prevent attempting to connect to a device which does not exist
	device = str(self.comboBoxPortSelect.currentText())
	if device == 'N/A':
		self.pushButtonDeviceConnect.setChecked(False)	
		return
	if (sys.platform != 'win32'):
		if ((not device.startswith(DEVICE_PATH)) or \
		    (not os.path.exists(device))):
			self.searchForDevices()
			self.pushButtonDeviceConnect.setChecked(False)
			return
        '''
	# initalize wheelchair control	
	self.wheelchair = \
                        wheelchair_control.capstone_program_wheelchair_control( \
                            device_address=device, \
                            command=None, \
                            DEBUG=self.DEBUG)
        '''
        # set callbacks
	self.disconnect(self.pushButtonDeviceConnect, \
                        QtCore.SIGNAL("clicked()"), \
			self.connectToWheelchair)
	self.connect(self.pushButtonDeviceConnect, \
                     QtCore.SIGNAL("clicked()"), \
                     self.disconnectFromWheelchair)

	# Change connect button text for next state	
	self.pushButtonDeviceConnect.setText('Disconnect')

	# disable the wheelchair connection options	
	self.comboBoxDeviceSelect.setEnabled(False)
	self.comboBoxPortSelect.setEnabled(False)
	self.pushButtonDeviceSearch.setEnabled(False)

	# enable the drive controls
	self.pushButtonForward.setEnabled(True)
	self.pushButtonReverse.setEnabled(True)
	self.pushButtonLeft.setEnabled(True)
	self.pushButtonRight.setEnabled(True)
	self.pushButtonStop.setEnabled(True)
	self.dialSpeed.setEnabled(True)

	# update status label
	self.labelWheelchairStatus.setText("Status: Connected")

	''' implement later	
	# Safety Measure: Explicitely require wheelchair speed control
	# to be enabled each time it wheelchair is connected
	self.pushButtonWheelchairSpeedEnable.setChecked(False)
	self.pushButtonWheelchairSpeedEnable.setText('Disabled')
	self.progressBarWheelchairSpeed.setValue(0)
	'''

    #####################################################################

    def disconnectFromWheelchair(self):

        # stop the wheelchair
        self.stopWheelchair()

        # set callbacks
        self.disconnect(self.pushButtonDeviceConnect, \
                        QtCore.SIGNAL("clicked()"), \
                        self.disconnectFromWheelchair)
	self.connect(self.pushButtonDeviceConnect, \
                     QtCore.SIGNAL("clicked()"), \
                     self.connectToWheelchair)

        # Change connect button text for next state 	
	self.pushButtonDeviceConnect.setText('Connect')

        # enable the wheelchair connection options
	self.comboBoxDeviceSelect.setEnabled(True)
	self.comboBoxPortSelect.setEnabled(True)
	self.pushButtonDeviceSearch.setEnabled(True)

	# disable the drive controls
	self.pushButtonForward.setEnabled(False)
	self.pushButtonReverse.setEnabled(False)
	self.pushButtonLeft.setEnabled(False)
	self.pushButtonRight.setEnabled(False)
	self.pushButtonStop.setEnabled(False)
	self.dialSpeed.setEnabled(False)

	# update status label
	self.labelWheelchairStatus.setText("Status: Disconnected")

        ''' implement later
        # Safety Measure: Explicitely require wheelchair speed control
	# to be enabled each time it wheelchair is connected
	self.pushButtonWheelchairSpeedEnable.setChecked(False)
	self.pushButtonWheelchairSpeedEnable.setText('Disabled')
	self.progressBarWheelchairSpeed.setValue(0)
	'''

    #####################################################################

    def connectWidgets(self):

        ## Global Buttons ##

        # set Tab key callback and action
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("Tab"))
	self.connect(action, QtCore.SIGNAL("triggered()"), self.rotateTabs)
	self.addAction(action)
	

        ## Wheelchair Buttons ##
	
	# Set drive control callbacks	
	self.connect(self.pushButtonForward, \
                     QtCore.SIGNAL("pressed()"), \
                     self.driveWheelchairForward)
	self.connect(self.pushButtonReverse, \
                     QtCore.SIGNAL("pressed()"), \
                     self.driveWheelchairReverse)	
	self.connect(self.pushButtonLeft, \
                     QtCore.SIGNAL("pressed()"), \
                     self.driveWheelchairLeft)	
	self.connect(self.pushButtonRight, \
                     QtCore.SIGNAL("pressed()"), \
                     self.driveWheelchairRight)
	self.connect(self.pushButtonStop, \
                     QtCore.SIGNAL("pressed()"), \
                     self.stopWheelchair)

	# set wheelchair button actions
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("w"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonForward, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("s"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonReverse, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("a"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonLeft, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("d"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonRight, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("Space"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonStop, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)	
		
		
	## Control Panel Buttons ##

	# set device callbacks
	self.connect(self.pushButtonDeviceSearch, \
                     QtCore.SIGNAL("clicked()"), \
                     self.searchForDevices)
	self.connect(self.pushButtonDeviceConnect, \
                     QtCore.SIGNAL("clicked()"), \
                     self.connectToWheelchair)

        # set message callbacks
        self.connect(self.setMsgDest, \
                     QtCore.SIGNAL("clicked()"), \
                     self.setMessageDestination)
	self.connect(self.clearMsgDest, \
                     QtCore.SIGNAL("clicked()"), \
                     self.clearMessageDestination)


	## Message Buttons ##
	
	# set keyboard button callbacks
	# numbers
	self.connect(self.keyboardNum1, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('1'))
	self.connect(self.keyboardNum2, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('2'))
	self.connect(self.keyboardNum3, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('3'))
	self.connect(self.keyboardNum4, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('4'))
	self.connect(self.keyboardNum5, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('5'))
	self.connect(self.keyboardNum6, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('6'))
	self.connect(self.keyboardNum7, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('7'))
	self.connect(self.keyboardNum8, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('8'))
	self.connect(self.keyboardNum9, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('9'))
	self.connect(self.keyboardNum0, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('0'))
	# letters
	self.connect(self.keyboardQ, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('Q'))
	self.connect(self.keyboardW, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('W'))
	self.connect(self.keyboardE, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('E'))
	self.connect(self.keyboardR, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('R'))
	self.connect(self.keyboardT, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('T'))
	self.connect(self.keyboardY, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('Y'))
	self.connect(self.keyboardU, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('U'))
	self.connect(self.keyboardI, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('I'))
	self.connect(self.keyboardO, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('O'))
	self.connect(self.keyboardP, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('P'))
	self.connect(self.keyboardA, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('A'))
	self.connect(self.keyboardS, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('S'))
	self.connect(self.keyboardD, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('D'))
	self.connect(self.keyboardF, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('F'))
	self.connect(self.keyboardG, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('G'))
	self.connect(self.keyboardH, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('H'))
	self.connect(self.keyboardJ, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('J'))
	self.connect(self.keyboardK, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('K'))
	self.connect(self.keyboardL, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('L'))
	self.connect(self.keyboardZ, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('Z'))
	self.connect(self.keyboardX, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('X'))
	self.connect(self.keyboardC, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('C'))
	self.connect(self.keyboardV, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('V'))
	self.connect(self.keyboardB, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('B'))
	self.connect(self.keyboardN, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('N'))
	self.connect(self.keyboardM, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('M'))
	# special characters
	self.connect(self.keyboardPeriod, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('.'))
	self.connect(self.keyboardComma, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage(','))
	self.connect(self.keyboardApostrophe, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage("'"))
	self.connect(self.keyboardQuestionMark, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('?'))
	self.connect(self.keyboardLeftParen, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('('))
	self.connect(self.keyboardRightParen, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage(')'))
	self.connect(self.keyboardColon, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage(':'))
	self.connect(self.keyboardSemiColon, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage(';'))
	self.connect(self.keyboardExclamationMark, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('!'))
	self.connect(self.keyboardSlash, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('/'))
	# backspace
	self.connect(self.keyboardBackspace, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('Backspace'))
	# space
	self.connect(self.keyboardSpace, \
                     QtCore.SIGNAL("clicked()"), \
                     lambda: self.addCharToMessage('Space'))
        # clear message
	self.connect(self.messageClearButton, \
                     QtCore.SIGNAL("clicked()"), \
                     self.clearMessage)
        
        # set select key callbacks
	self.connect(self.keyboardSelectLeft, \
                     QtCore.SIGNAL("clicked()"), \
                     self.selectLeftKeys)
        self.connect(self.keyboardSelectRight, \
                     QtCore.SIGNAL("clicked()"), \
                     self.selectRightKeys)
        
        # set select key actions          
        action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("q"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.keyboardSelectLeft, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("e"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.keyboardSelectRight, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)

	# send message button
	self.connect(self.messageSendButton, \
                     QtCore.SIGNAL("clicked()"), \
                     self.sendUserMessage)


	## Reserved ##
	
		
    #####################################################################

    def searchForDevices(self):

        wheelchair_devices = []

        # List all serial devices
	serial_devices = self.enumerateSerialPorts()

	for serial_device in serial_devices:
            wheelchair_devices.append(serial_device)

        # Configure combo box
        if wheelchair_devices == []:
            wheelchair_devices.append('N/A')
        
        if self.pushButtonDeviceConnect.text != 'Disconnect':
            self.comboBoxPortSelect.clear()
            
            for wheelchair in wheelchair_devices:
                self.comboBoxPortSelect.addItem(wheelchair)
        
    #####################################################################

    def enumerateSerialPorts(self):

        """ Uses the Win32 registry to return an iterator of serial (COM) ports
            existing on this computer.
	    From:
	    http://eli.thegreenplace.net/2009/07/31/listing-all-serial-ports-on-windows-with-python/
	"""
        
	serial_ports = []
		
	if (sys.platform == 'win32'):
            
            path = 'HARDWARE\\DEVICEMAP\\SERIALCOMM'
            
            try:
                key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, path)
            except WindowsError:
                return []
            
            for i in itertools.count():
                try:
                    val = winreg.EnumValue(key, i)
                    serial_ports.append( str(val[1]) )
		except EnvironmentError:
                    break
                
	else:
            if os.path.exists(DEVICE_PATH):
                
                device_list = os.listdir(DEVICE_PATH)
                device_list.sort()
                
                for device in device_list:
                    if device.startswith('ttyUSB'):
                        serial_ports.append( DEVICE_PATH + '/' + device )
                for device in device_list:
                    if device.startswith('rfcomm'):
                        serial_ports.append( DEVICE_PATH + '/' + device )
                for device in device_list:
		    if device.startswith('ttyACM'):
			serial_ports.append( DEVICE_PATH + '/' + device )
		for device in device_list:
                    if device.startswith('ttyS'):
                        serial_ports.append( DEVICE_PATH + '/' + device )
		for device in device_list:
                    if device.startswith('tty.NXT-DevB'):
                        serial_ports.append( DEVICE_PATH + '/' + device )
            
	return(serial_ports)

    #####################################################################

    def fullPortName(self, portname):
        
        """ Given a port-name (of the form COM7, COM12, CNCA0, etc.)
            returns a full name suitable for opening with the Serial class.
	"""

	m = re.match('^COM(\d+)$', portname)
	if m and int(m.group(1)) < 10:
            return portname
		
	return '\\\\.\\' + portname

    #####################################################################

    ## Wheelchair Drive Commands ##
    
    def driveWheelchairForward(self):
        #print "WheelchairForward"
        self.sendCommand('w')
	
    def driveWheelchairReverse(self):
        #print "WheelchairReverse"
        self.sendCommand('s')
	
    def driveWheelchairLeft(self):
        #print "WheelchairLeft"
        self.sendCommand('a')
	
    def driveWheelchairRight(self):
        #print "WheelchairRight"
        self.sendCommand('d')
	
    def stopWheelchair(self):
        #print "stopWheelchair"
        self.sendCommand(' ')

    #####################################################################

    def sendCommand(self, command):

        # get the port name
        port = str(self.comboBoxPortSelect.currentText())

        # open the port
        ser = serial.Serial(port)

        # write command
        ser.write(command)

        # read up to ten bytes (timeout)
        s = ser.read(10)

        # read a '\n' terminated line
        line = ser.readline()

        # close port
        ser.close()

    #####################################################################

    def updateWheelchairSpeed(self, new_speed=None):

        if new_speed == None:
            
            new_speed = self.calculateSpeed()

        # Update GUI
        self.dialSpeed.setValue(new_speed)

        self.current_speed = new_speed

    #####################################################################

    def calculateSpeed(self):


        '''
        Will need to pull data from sensors and motors and do speed stuff here?
        '''
        
        speed = 0
        
	return(speed)

    #####################################################################

    def rotateTabs(self):

        # get the total number of tabs
        # NOTE: count returns N (0 to N-1 tabs)
        count = self.tabWidget.count()

        # get the tab we are currently on
        index = self.tabWidget.currentIndex()

        # if index is equal to the count...
        if (index == count-1):
            # reset the index
            index = 0
        else:
            # increment the index
            index = index + 1

        # set the new tab as the current tab
        self.tabWidget.setCurrentIndex(index)

    #####################################################################

    def setMessageDestination(self):
        
        global MESSAGE_DESTINATION
        
        # get destination type
        destType = str(self.selectDestType.currentText())

        # get the text from the message destination line edit box
        destination = str(self.lineEditMsgDest.text())
        
        # if we have a phone number...
        if destType == 'Phone Number':
        
            # get the carrier
            carrier = str(self.selectPhoneCarrier.currentText())

            # build MESSAGE_DESTINATION string
            if   carrier == 'AT&T':
                MESSAGE_DESTINATION = str(destination+'@txt.att.net')
            elif carrier == 'Sprint':
                MESSAGE_DESTINATION = str(destination+'@messaging.sprintpcs.com')
            elif carrier == 'T-Mobile':
                MESSAGE_DESTINATION = str(destination+'@tmomail.net')
            elif carrier == 'Verizon':
                MESSAGE_DESTINATION = str(destination+'@vtext.com')

        else:
            # we have an email address
            MESSAGE_DESTINATION = destination

    #####################################################################

    def clearMessageDestination(self):

        global MESSAGE_DESTINATION

        # clear the message destination line edit text
        MESSAGE_DESTINATION = ''

        # update the line edit text
        self.lineEditMsgDest.setText(MESSAGE_DESTINATION)
    
    #####################################################################

    def sendUserMessage(self):

        global USER_MESSAGE

        if USER_MESSAGE == '':
            # prevent sending message when nothing has been typed
            USER_MESSAGE = USER_MESSAGE
            
        else:
            # Send text in the messageTextBox to the given destination
            ms.sendMessage(MESSAGE_DESTINATION, USER_MESSAGE)

            # clear the message after being sent
            self.clearMessage()

    #####################################################################

    def addCharToMessage(self, key):

        global USER_MESSAGE

        # if backspace, pop last char
        if key == 'Backspace':
            USER_MESSAGE = USER_MESSAGE[:-1]

        else:
            # if space, use ' '
            if key == 'Space':
                key = ' '

            # append char to end of current message
            USER_MESSAGE = USER_MESSAGE+key

        # update the line edit text
        self.messageTextBox.setText(USER_MESSAGE)

    #####################################################################

    def clearMessage(self):
        
        global USER_MESSAGE

        # clear the user message line edit text
        USER_MESSAGE = ''

        # update the line edit text
        self.messageTextBox.setText(USER_MESSAGE)

    #####################################################################

    def selectLeftKeys(self):

        global TYPING, IMPORTED_KEYS

        if TYPING == True:

            # red keys are eliminated, set to clear
            self.repaintKeys(RED_KEYS, BLANK)
            
            # split the blue keys
            self.selector.select(False)

            if self.selector.getChoiceCount() == 1:
                # send click
                BLUE_KEYS.pop().click()

                # refresh Becker's class
                self.selector.reset()
                
                # refresh dict
                IMPORTED_KEYS = {}
                
                # prepare for a new round
                self.keyboardSelectRight.setText("Next")
                self.repaintKeys(self.keyboardDict.values(), BLUE)
                
                TYPING = False
                
                return

            else:
                # fill IMPORTED_KEYS
                IMPORTED_KEYS = self.selector.splitChoices()

                # separate new choices
                self.mapKeys(IMPORTED_KEYS)
                
                # redraw
                self.repaintKeys(BLUE_KEYS, BLUE)
                self.repaintKeys(RED_KEYS, RED)

        if TYPING == False:

            # loop through and click the selected button
            if CLICKS == 1:
                # begin keyboard operation
                self.groupBox_keyboard.setStyleSheet(BLANK)
                self.keyboardSelectRight.setText("Select")
                CHOICE = False

                # fill IMPORTED_KEYS
                IMPORTED_KEYS = self.selector.splitChoices()

                # separate IMPORTED_KEYS into red and blue choices
                self.mapKeys(IMPORTED_KEYS)

                # paint keys the appropriate color
                self.repaintKeys(RED_KEYS, RED)
                self.repaintKeys(BLUE_KEYS, BLUE)

                TYPING = True
                
            elif CLICKS == 2:
                # send Backspace a click
                self.keyboardBackspace.click()
            elif CLICKS == 3:
                # send Clear a click
                self.messageClearButton.click()
            elif CLICKS == 4:
                # send Send a click
                self.messageSendButton.click()
        

    #####################################################################

    def selectRightKeys(self):

        global CLICKS, TYPING, IMPORTED_KEYS

        if TYPING == False:

            # loop through and change the style sheet based on what's selected
            if CLICKS == 1:
                # Highlight Backspace
                self.repaintKeys(self.keyboardDict.values(), BLANK)
                self.keyboardBackspace.setStyleSheet(BLUE)
                
            elif CLICKS == 2:
                # Highlight Clear
                self.keyboardBackspace.setStyleSheet(BLANK)
                self.messageClearButton.setStyleSheet(BLUE)
                
            elif CLICKS == 3:
                # Highlight Send
                self.messageClearButton.setStyleSheet(BLANK)
                self.messageSendButton.setStyleSheet(BLUE)
                
            elif CLICKS == 4:
                # Highlight Keyboard
                self.messageSendButton.setStyleSheet(BLANK)
                self.repaintKeys(self.keyboardDict.values(), BLUE)
                
                CLICKS = 0
            
            CLICKS = CLICKS +1
            
        if TYPING == True:

            # blue keys are eliminated, set to clear
            self.repaintKeys(BLUE_KEYS, BLANK)
            
            # split the red keys
            self.selector.select(True)

            # Check if single button is left
            if self.selector.getChoiceCount() == 1:
                # send click
                RED_KEYS.pop().click()

                # refresh Becker's class
                self.selector.reset()
                
                # refresh dict
                IMPORTED_KEYS = {}

                # prepare for a new round
                self.keyboardSelectRight.setText("Next")
                self.repaintKeys(self.keyboardDict.values(), BLUE)
                
                TYPING = False
                
                return
            
            else:
                # fill IMPORTED_KEYS
                IMPORTED_KEYS = self.selector.splitChoices()

                # separate new choices
                self.mapKeys(IMPORTED_KEYS)

                # redraw
                self.repaintKeys(BLUE_KEYS, BLUE)
                self.repaintKeys(RED_KEYS, RED)

    #####################################################################

    def repaintKeys(self, keys, color):

        # paints the given keys the selected color
        for i in keys:
            i.setStyleSheet(color)
        
    #####################################################################

    def mapKeys(self, keys):

        global BLUE_KEYS, RED_KEYS

        # map the buttons to True or False
        temp = {self.keyboardDict[i]:keys[i] for i in keys \
                if i in self.keyboardDict}

        # separate True and False
        RED_KEYS = {i for i in temp if temp[i] == True}
        BLUE_KEYS = {i for i in temp if temp[i] == False}

    #####################################################################

    #
    
    #####################################################################

    def closeEvent(self, event):
        
        quit_message = "Are you sure you want to exit the program?"
        
        reply = QtGui.QMessageBox.question(self, \
                                           'Quit Capstone C6', \
                                           quit_message, \
                                           QtGui.QMessageBox.Yes, \
                                           QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            # Quit
            event.accept()

        else:
            # Cancel
            event.ignore()


#####################################################################
# Main
#####################################################################

if __name__ == '__main__':

    log = None
	
    app = QtGui.QApplication(sys.argv)
	
    window = capstone_program_client_interface(log, DEBUG)
    window.show()
	
    sys.exit(app.exec_())
