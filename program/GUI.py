# GUI.py
#
#

import os, sys, time

if (sys.platform == 'win32'):
    DEFAULT_IMAGE_PATH = 'images'
    import _winreg as winreg
    import itertools
    import re
    import serial

import Configuration as configuration

from PyQt4 import QtCore, QtGui, QtNetwork

from GUI_Design import Ui_Form as Design

import Client as client
import Wheelchair_Control as wheelchair_control
import MessageSender as ms

#####################################################################
# GLOBALS
#####################################################################

DEBUG = 1

DEVICE_PATH = ''

USER_MESSAGE = ''

#####################################################################
# CLASSES
#####################################################################

class capstone_client_interface(Qt.Gui.QWidget, Design):
    def __init__(self, log, server=None, DEBUG=DEBUG, parent=None):
        self.log = log
        self.DEBUG = DEBUG

        QtGui.QWidget.__init__(self, parent)
        self.setupUi(self)

        self.configureSettings()
        self.connectWidgets()

        self.name = "Capstone Interface"

        self.robot_type = None
		
	self.brainstormsServer = server
	self.brainstormsClient = None
	
	self.wheelchair = None
		
	self.drive_state = 'stop_motors'
	self.current_speed = 0

    #####################################################################

    def configureSettings(self):

        ## Capstone Interface ##

        # Load the window icon
        image_path = "puzzlebox.ico"
	if not os.path.exists(image_path):
            image_path = os.path.join(DEFAULT_IMAGE_PATH, image_path)
		
	if os.path.exists(image_path):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(image_path), \
                           QtGui.QIcon.Normal, \
                           QtGui.QIcon.Off)
            self.setWindowIcon(icon)

	# Search for available Serial devices
	self.searchForDevices()

        ## Wheelchair ##

        # Set status message
	self.labelWheelchairStatus.setText("Status: Disconnected")
	
	# Disable the drive controls
	self.pushButtonForward.setEnabled(False)
        self.pushButtonLeft.setEnabled(False)
	self.pushButtonRight.setEnabled(False)
	self.pushButtonReverse.setEnabled(False)
	
        ## Control Panel ##

	# add control panel stuff here if needed

	
    #####################################################################

    def connectToWheelchair(self):
        
        # Prevent attempting to connect to a device which does not exist
	device = str(self.comboBoxWheelchairPortSelect.currentText())
	if device == 'N/A':
		self.pushButtonDeviceConnect.setChecked(False)	
		return
	if (sys.platform != 'win32'):
		if ((not device.startswith(DEVICE_PATH)) or \
		    (not os.path.exists(device))):
			self.searchForDevices()
			self.pushButtonDeviceConnect.setChecked(False)
			return

	# 	
	self.wheelchair = \
	   wheelchair_control.capstone_wheelchair_control( \
	      device_address=device,
	      command=None, \
	      DEBUG=self.DEBUG)

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
	self.comboBoxWheelchairTransmitter.setEnabled(False)
	self.comboBoxWheelchairPortSelect.setEnabled(False)
	self.pushButtonWheelchairSearch.setEnabled(False)

	# enable the drive controls
	self.pushButtonForward.setEnabled(True)
	self.pushButtonReverse.setEnabled(True)
	self.pushButtonLeft.setEnabled(True)
	self.pushButtonRight.setEnabled(True)
	self.pushButtonStop.setEnabled(True)
	self.dialSpeed.setEnabled(True)

	''' implement later	
	# Safety Measure: Explicitely require wheelchair speed control
	# to be enabled each time it wheelchair is connected
	self.pushButtonWheelchairSpeedEnable.setChecked(False)
	self.pushButtonWheelchairSpeedEnable.setText('Disabled')
	self.progressBarWheelchairSpeed.setValue(0)
	'''

    #####################################################################

    def disconnectFromWheelchair(self):

        self.stopWheelchair()

        self.disconnect(self.pushButtonWheelchairConnect, \
                        QtCore.SIGNAL("clicked()"), \
                        self.disconnectFromWheelchair)
		
	self.connect(self.pushButtonWheelchairConnect, \
                     QtCore.SIGNAL("clicked()"), \
                     self.connectToWheelchair)
		
	self.pushButtonWheelchairConnect.setText('Connect')

	self.comboBoxWheelchairTransmitter.setEnabled(True)
	self.comboBoxWheelchairPortSelect.setEnabled(True)
	self.pushButtonWheelchairSearch.setEnabled(True)
	
	self.pushButtonWheelchairForward.setEnabled(False)
	self.pushButtonWheelchairReverse.setEnabled(False)
	self.pushButtonWheelchairLeft.setEnabled(False)
	self.pushButtonWheelchairRight.setEnabled(False)
	self.pushButtonWheelchairStop.setEnabled(False)
	self.dialWheelchairSpeed.setEnabled(False)

        ''' implement later
        # Safety Measure: Explicitely require wheelchair speed control
	# to be enabled each time it wheelchair is connected
	self.pushButtonWheelchairSpeedEnable.setChecked(False)
	self.pushButtonWheelchairSpeedEnable.setText('Disabled')
	self.progressBarWheelchairSpeed.setValue(0)
	'''

    #####################################################################

    def connectWidgets(self):

        # Wheelchair Buttons
	
		
	'''	
	self.connect(self.pushButtonWheelchairConcentrationEnable, \
                     QtCore.SIGNAL("clicked()"), \
                     self.updateWheelchairConcentrationButton)
		
	self.connect(self.pushButtonWheelchairRelaxationEnable, \
                     QtCore.SIGNAL("clicked()"), \
                     self.updateWheelchairRelaxationButton)
	'''	
	self.connect(self.pushButtonWheelchairSpeedEnable, \
                     QtCore.SIGNAL("clicked()"), \
                     self.updateWheelchairSpeedButton)
		
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
		
		
		
	# Control Panel Buttons
	self.connect(self.pushButtonDeviceSearch, \
                     QtCore.SIGNAL("clicked()"), \
                     self.searchForDevices)
	
	self.connect(self.pushButtonDeviceConnect, \
                     QtCore.SIGNAL("clicked()"), \
                     self.connectToWheelchair)
	
		
	# Global Buttons
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("Tab"))
	self.connect(action, QtCore.SIGNAL("triggered()"), self.rotateControlButtons)
	self.addAction(action)

        # Wheelchair Buttons
        '''
            Might change to WASD
        '''
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("i"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonForward, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("k"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonReverse, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("j"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonLeft, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("l"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonRight, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)
		
	action = QtGui.QAction(self)
	action.setShortcut(QtGui.QKeySequence("Space"))
	self.connect(action, QtCore.SIGNAL("activated()"), self.pushButtonStop, \
                     QtCore.SLOT("animateClick()"))
	self.addAction(action)

	# Message Buttons
	self.connect(self.keyboardNum1, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum2, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum3, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum4, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum5, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum6, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum7, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum8, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum9, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.keyboardNum0, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	self.connect(self.# PUT KEYBOARD KEYS HERE, \
                     QtCore.SIGNAL("clicked()"), \
                     self.addCharToMessage)
	
		
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

        if self.pushButtonWheelchairConnect.text != 'Disconnect':
            self.comboBoxWheelchairPortSelect.clear()
            
            for wheelchair in wheelchair_devices:
                self.comboBoxWheelchairPortSelect.addItem(wheelchair)

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

    def driveWheelchairForward(self):
        #print "WheelchairForward"
        speed = self.dialWheelchairSpeed.value()
        self.wheelchair.sendCommand(speed, 'forward')
	
    def driveWheelchairReverse(self):
        #print "WheelchairReverse"
        speed = self.dialWheelchairSpeed.value()
        self.wheelchair.sendCommand(speed, 'reverse')
	
    def driveWheelchairLeft(self):
        #print "WheelchairLeft"
        speed = self.dialWheelchairSpeed.value()
        self.wheelchair.sendCommand(speed, 'left')
	
    def driveWheelchairRight(self):
        #print "WheelchairRight"
        speed = self.dialWheelchairSpeed.value()
        self.wheelchair.sendCommand(speed, 'right')
	
    def stopWheelchair(self):
        #print "stopWheelchair"
        speed = self.dialWheelchairSpeed.value()
        self.wheelchair.sendCommand(speed, 'stop')
    

    #####################################################################

    def  updateWheelchairSpeed(self, new_speed=None):

        if new_speed == None:

            ''' Will need to pull data from sensors and motors and do speed stuff here
            '''
            concentration = self.progressBarWheelchairConcentration.value()
            relaxation = self.progressBarWheelchairRelaxation.value()
            
            new_speed = self.calculateSpeed(concentration, relaxation)

        # Update GUI
        if self.pushButtonWheelchairSpeedEnable.isChecked():
            self.progressBarWheelchairSpeed.setValue(new_speed)

        self.current_speed = new_speed

    #####################################################################

    def  calculateSpeed(self, concentration, relaxation):

        speed = 0
        # check if we need calculations first
        ''' 
        thresholds = define thresholds first

        match = int(concentration)

	while ((match not in thresholds['concentration'].keys()) and (match >= 0)):
            match -= 1

	if match in thresholds['concentration'].keys():
            speed = thresholds['concentration'][match]
		
        match = int(relaxation)

        while ((match not in thresholds['relaxation'].keys()) and (match >= 0)):
            match -= 1
		
	if match in thresholds['relaxation'].keys():
        '''
	return(speed)
    
    #####################################################################

    def  sendUserMessage(self):

        # Send text in the messageTextBox to the given destination
        
        toNumber = #given phone number
        ms.sendMessage(toNumber, USER_MESSAGE)

    #####################################################################

    def addCharToMessage(self, button):
        # get pressed key text string 
        key = self.button.getText()

        # if backspace, pop last char
        if key == Backspace:
            USER_MESSAGE = USER_MESSAGE[:-1]

        else:
            # if space, use ' '
            if key == Space
                key = ' '

            # append char to end of current message
            USER_MESSAGE = USER_MESSAGE+key
        

    #####################################################################

    def  closeEvent(self, event):
        
        quit_message = "Are you sure you want to exit the program?"
        
        reply = QtGui.QMessageBox.question(self, \
                                           'Quit C6 Capstone', \
                                           quit_message, \
                                           QtGui.QMessageBox.Yes, \
                                           QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            if self.brainstormsClient != None:
                
                self.stopMotors()
                self.brainstormsClient.socket.flush()
                '''
                if self.brainstormsServer != None:
                    if self.brainstormsServer.rc == None:
                        
                        device_address = str(self.comboBoxRobotPortSelect.currentText())
                        elf.brainstormsServer.executeCommand('stop_motors')
                        
                    else:
                        self.brainstormsServer.rc.run('stop_motors')
                '''
                        
            event.accept()

        else:
            event.ignore()


#####################################################################
# Main
#####################################################################

if __name__ == '__main__':
	
	#log = puzzlebox_logger.puzzlebox_logger(logfile='client_interface')
	log = None
	
	app = QtGui.QApplication(sys.argv)
	
	window = capstone_client_interface(log, DEBUG)
	window.show()
	
	sys.exit(app.exec_())
