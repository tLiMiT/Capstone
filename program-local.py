# program-local.py
#
#

__changelog__ = """\
Last Update: 
"""

__doc__ = """|
Hope this works
"""

import os, sys
import signal

from PyQt4 import QtCore, QtGui, QtNetwork

import capstone.program.Configuration as configuration
import capstone.program.GUI as GUI
import capstone.program.Client as client

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

    # 
	
    app = QtGui.QApplication(sys.argv)

    window = GUI.capstone_client_interface(log, \
                                           server=None, \
                                           DEBUG=DEBUG)

    window.show()

    sys.exit(app.exec_())
