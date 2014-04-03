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

        # Remove the build folder, a bit slower but ensures that build contains the latest
        shutil.rmtree("build", ignore_errors=True)
    
        options={"py2exe": \
                 {"includes": [ \
                         "sip", \
                         "PySide.QtSvg", \
                         ], \
                  "excludes": [ \
                          "bluetooth", "tcl", \
                          '_gtkagg', '_tkagg', '_agg2', \
                          '_cairo', '_cocoaagg', \
                          '_fltkagg', '_gtk', '_gtkcairo'], \
                  "dll_excludes": [ \
                          'tcl84.dll', 'tk84.dll' \
                          'libgdk-win32-2.0-0.dll', \
                          "MSVCP90.dll", \
                          'libgobject-2.0-0.dll'], \
                  "compressed": 2, \
                  "optimize": 2, \
                  "bundle_files": 3, \
                  "dist_dir": "dist", \
                  "xref": False, \
                  "skip_archive": False, \
                  }
        }

        data_files=[(".", \
                     ["capstone_program_configuration.ini"]),
                    ("images", \
                     ["images/puzzlebox.ico", \
                      "images/forward.svg", \
                      "images/reverse.svg", \
                      "images/left.svg", \
                      "images/right.svg", \
                      "images/stop.svg",
                      ]),
                    ("capstone/program", \
                     ["capstone/program/CharFreqBinary_f_base.bin"]),
                    ]
    
else:
        options={}

        # Reserved for non-Windows OS
        data_files=[]


setup(
        name='capstone_program',
        version='0.1',
        description='A Brain-Computer Interface (BCI) control for an electric wheelchair',
        author='2014 NEU Capstone Team C6',
        author_email='',
        url='',
        py_modules=['capstone', \
                    'capstone.program', \
                    'capstone.program.CharacterFreqLogger', \
                    'capstone.program.Client', \
                    'capstone.program.Configuration', \
                    'capstone.program.GUI', \
                    'capstone.program.GUI_Design', \
                    'capstone.program.MessageSender', \
                    'capstone.program.TextInserter', \
#                    'capstone.program.TextTester', \
                    'capstone.program.Wheelchair_Control', \
                    'program-local', \
        ], \
        console=["program-local.py", \
#                 ""
        ], \
        options=options, \
        zipfile = r'lib\library.zip',
        data_files=data_files, \
        windows=[{ \
                  "script":             "program-local.py",
                  "icon_resources":     [(1, os.path.join("images", "puzzlebox.ico"))]
                  },
        ], \
        classifiers=['Development Status :: Prototype/Demo',
                     'Intended Audience :: End Users/Desktop',
                     'Programming Language :: Python',
                     'Operating System :: OS Independent',
                     'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        ], \
)
    
