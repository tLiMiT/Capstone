# Configuration.py
#
#

import os, sys

#####################################################################
# General configuration
#####################################################################

DEBUG = 1

ENABLE_CONTROL_PANEL = True

CONFIGURATION_FILE_PATH = 'capstone_configuration.ini'

if (sys.platform != 'win32'):
    if not os.path.exists(CONFIGURATION_FILE_PATH):
        # edit path if needed
        CONFIGURATION_FILE_PATH = os.path.join('path', CONFIGURATION_FILE_PATH)

#####################################################################
# Logging
#####################################################################

LOG_LEVEL_DEBUG = 2
LOG_LEVEL_INFO = 1
LOG_LEVEL_ERROR = 0
LOG_LEVEL_DISABLE = -1

DEFAULT_LOG_LEVEL = LOG_LEVEL_DEBUG
DEFAULT_LOGFILE = 'brainstorms'

LOGFILE_DIR = '/var/log/puzzlebox'
LOGFILE_SUFFIX = '.log'
LOGFILE_SUFFIX_DEBUG = '_debug.log'
LOGFILE_SUFFIX_INFO = '_info.log'
LOGFILE_SUFFIX_ERROR = '_error.log'

SPLIT_LOGFILES = False

#####################################################################
# Client configuration
#####################################################################

CLIENT_NO_REPLY_WAIT = 5 # how many seconds before considering a component dead

#####################################################################
# Client Interface configuration [Qt]
#####################################################################

# reserved for later

#####################################################################
# Configuration File Parser
#####################################################################

if os.path.exists(CONFIGURATION_FILE_PATH):

    file = open(CONFIGURATION_FILE_PATH, 'r')

    for line in file.readlines():
        
        line = line.strip()
        
        if len(line) == 0:
            continue
        if line[0] == '#':
            continue
        
        try:
            exec line
        except:
            if DEBUG:
                print "Error recognizing configuration option:",
                print line


