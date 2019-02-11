import cx_Freeze
import os

os.environ['TCL_LIBRARY'] = "C:\\Users\\willi\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tcl8.6"
os.environ['TK_LIBRARY'] = "C:\\Users\\willi\\AppData\\Local\\Programs\\Python\\Python37-32\\tcl\\tk8.6"

executables = [cx_Freeze.Executable("PixelClick.py")]

cx_Freeze.setup(
    name = "Pixel Click",
    author = "William Culver",
    options = {"build_exe": {"packages": ["pygame"],
                             "include_files": ["freesansbold.ttf", "images/", "sounds/", "README.txt"]}},
    executables = executables
)