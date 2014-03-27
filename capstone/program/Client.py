# Client.py
#
#

import os, sys
import signal

import Configuration as configuration

from PyQt4 import QtCore, QtGui, QtNetwork

#import simplejson as json


#####################################################################
# Globals
#####################################################################

DEBUG = 1


#####################################################################
# Main
#####################################################################

if __name__ == '__main__':
	
	# Perform correct KeyboardInterrupt handling
	signal.signal(signal.SIGINT, signal.SIG_DFL)

	
