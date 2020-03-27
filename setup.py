#This cx_Freeze script converts python tkinter app to .exe
#Write the following command to execute this file
#python setup.py build

from cx_Freeze import setup, Executable
import os
import sys

base = None    

if (sys.platform == "win32"):
    base = "Win32GUI" 

executables = [Executable("CoronaVirusTracker.py", base=base)]

packages = ["idna" , "tkinter", "bs4", "requests", "threading"] #Packages you have used in your app and don't remove "idna"
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "Corona Virus Case Counter",
    options = {'build_exe': {'includes': ["tkinter"], 'include_files':[
    (os.path.join('D:\Programming Languages\Python\Python38-32', 'DLLs', 'tk86t.dll'), os.path.join('lib', 'tk86t.dll')), #Give path to your own python direcotry
    (os.path.join('D:\Programming Languages\Python\Python38-32', 'DLLs', 'tcl86t.dll'), os.path.join('lib', 'tcl86t.dll')),
    'virus.ico',
    ]}},
    version = "1.0",
    description = 'This app provides a a fast way to get corona virus cases updates from important regions of the World.',
    executables = executables
)