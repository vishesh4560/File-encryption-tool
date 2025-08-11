# File Encryption Tool

## Overview
This is a simple GUI application for encrypting and decrypting files using symmetric encryption (Fernet/AES). The tool is built with Python and Tkinter, and is suitable for Windows.

## Features
- Generate a secure encryption key (`secret.key`)
- Encrypt any file using the generated key
- Decrypt files that were encrypted with the tool
- Simple graphical interface

## How to Use
1. **Generate Key**: Click "Generate Key" to create a new encryption key (`secret.key`).
2. **Encrypt File**: Click "Encrypt File" and select a file to encrypt. The file will be overwritten with its encrypted version.
3. **Decrypt File**: Click "Decrypt File" and select an encrypted file to decrypt. The file will be restored to its original content.
4. **Exit**: Click "Exit" to close the application.


## Requirements
- Python 3.x
- `cryptography` package
- Tkinter (included with most Python installations; if you get an error, run `pip install tk`)

Install dependencies:
```powershell
pip install -r requirements.txt
```

## Build EXE (Optional)
To build a standalone Windows executable:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole file_encryption_gui.py
```
The EXE will be created in the `dist` folder.

## Bug Reports & Contributing
- Please use the issue tracker for bug reports and feature requests.
- See `CONTRIBUTING.md` for guidelines on contributing.
- Use the provided templates for bug reports and pull requests.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.