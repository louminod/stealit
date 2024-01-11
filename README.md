# You want it ? Stealit !

# Overview
This is a Python script that listens for a certain keyboard key combination and triggers a screenshot. The screenshot is then processed to extract text from the image using OCR (Optical Character Recognition).

# Dependencies
- pynput
- pytesseract
- pyperclip
- subprocess
- PIL
- os

# Usage
This Python script uses the combination `Cmd+Shift+0` on macOS to trigger a screenshot.

When this key combination is pressed, a screenshot selection tool is opened up (via macOS's `screencapture` utility) and the selected area is captured as `screenshot.png` in the `/tmp` directory. The screenshot is then opened and stored in a `PIL` Image object before the original screenshot file is deleted.

The screenshot is then processed with the `pytesseract` library. This library uses Tesseract, a powerful OCR engine, to find and extract text from the screenshot. The extracted text is then copied to your clipboard using `pyperclip`, allowing you to paste it wherever you'd like.

# Limitations
Please note that this script is specifically designed to work on macOS and may not function as intended on other operating systems.

# Required Installation
This script requires the above-mentioned python libraries. These can be installed via pip (Python's package installer). Run the following command to install:

`$ pip install pynput pytesseract pyperclip pillow`

Also, note that the Tesseract OCR engine must be installed on your system for `pytesseract` to work. Refer to the `pytesseract` documentation or the Tesseract GitHub repo for installation instructions.