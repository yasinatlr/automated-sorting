
# Automated File Organization

## Introduction
The Automated File Organizer project aims to enhance digital workspace management through the automatic categorization and sorting of files. This tool is designed to bring efficiency and organization to the file management process, making it an ideal solution for both individuals and businesses looking to streamline their digital environments.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Customization](#customization)
- [License](#license)

## Installation
Before you can use the Automated File Organizer, make sure you have the following prerequisites installed:

Python 3.x: The script is written in Python, so you'll need Python installed on your system. You can download it from the official [Python](https://www.python.org/downloads/) website.
This script has been tested on Windows, macOS, and Linux. It should work on any platform that supports Python.

## Usage
To use the Automated File Organizer, follow these steps:

1. Open a terminal or command prompt.

2. Navigate to the directory where the automated_file_organizer.py script is located.

3. Run the script using Python. You will be prompted to enter the source directory path (where your unorganized files are located) and the destination directory path (where you want the organized files to be placed).
```
python automated_file_organizer.py
```
4. Follow the on-screen instructions to organize your files and review any files you might want to delete.

## Features
- File Organization: Automatically moves files into folders based on their extensions.
- Customizable Folders: Easily modify the script to create custom folders for different file types.
- Interactive File Deletion: Review and optionally delete files from the "Others" folder.

## Dependencies
No additional libraries are required for the basic functionality of this script. However, if you modify the script to include more complex features, you might need to install additional Python packages using pip. For example:
```
pip install some-package
```
## Customization
You can customize the script to fit your specific needs. For example, if you frequently work with .py (Python) files, you might want to add a "Code" category.

To do this, modify the file_extensions_and_folders dictionary in the script before running it:

```
file_extension_mapping = {
        ".pdf": "Documents", ".docx": "Documents", ".txt": "Documents", ".pptx": "Documents", ".xlsx": "Documents", ".csv": "Documents",
        ".jpg": "Images", ".jpeg": "Images", ".png": "Images", ".gif": "Images", ".bmp": "Images", ".tiff": "Images",
        ".mp4": "Videos", ".mov": "Videos", ".avi": "Videos", ".mkv": "Videos", ".flv": "Videos", ".wmv": "Videos",
        ".mp3": "Music", ".wav": "Music", ".aac": "Music", ".flac": "Music", ".ogg": "Music", ".wma": "Music",
        ".zip": "Archives", ".rar": "Archives", ".tar": "Archives", ".gz": "Archives", ".7z": "Archives",
        ".py": "Code", ".c": "Code", ".cpp": "Code", ".java": "Code", ".cs": "Code", ".html": "Code", ".css": "Code", ".js": "Code", ".php": "Code", ".sh": "Code", ".bat": "Code", ".ps1": "Code", ".cmd": "Code"
    }
```

## License
The Automated File Organizer is open-source software licensed under the MIT License.

```
MIT License

Copyright (c) [year] [Full name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

This license permits anyone to use, modify, and distribute the software for any purpose, commercial or non-commercial, provided they include the original copyright notice and the license text with any substantial portions of the Software. It also makes it clear that the software is provided "as is", without any warranty.
