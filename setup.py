# setup.py
#
#

from distutils.core import setup
import os, sys
import glob

if (sys.platform == 'win32'):
	import py2exe
	import shutil

#####################################################################
# Main
#####################################################################

if __name__ != '__main__':

	sys.exit()


if (sys.platform == 'win32'):
    # Reserved to clear build folders and clean up for .exe distribution
    options={}
    
else:
    options={}
    # Reserved to clear build folders and clean up for .exe distribution


setup(
    name='C6_Capstone_Program',
    version='0.1',
    description='A Brain-Computer Interface (BCI) control for an electric wheelchair',
    author='2014 NEU Capstone Team C6',
    author_email='',
    url='',
    py_modules=['', \
                '', \
    ], \
    console=["", \
             ""
    ],
    options=options, \
    zipfile = r'',
    data_files=data_files, \
    windows=[ {"script": "",
               "icon_resources": [(1, os.path.join("images", "puzzlebox.ico"))]
               },
    ],
    classifiers=['Development Status :: Prototype/Demo',
                 'Intended Audience :: End Users/Desktop',
                 'Programming Language :: Python',
                 'Operating System :: OS Independent',
                 'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    ]
)
    
