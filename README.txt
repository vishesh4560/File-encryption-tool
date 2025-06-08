
# File Encryption Tool - EXE Build Instructions

This folder contains the GUI version of the File Encryption Tool.

## How to Build the EXE (on Windows)

1. Open Command Prompt
2. Install PyInstaller (if not already installed):
   pip install pyinstaller

3. Navigate to this folder in CMD:
   cd path\to\this\folder

4. Build the EXE:
   pyinstaller --onefile --noconsole file_encryption_gui.py

5. After building, your EXE will appear in the 'dist' folder.

## Requirements
To install dependencies, run:
   pip install -r requirements.txt
