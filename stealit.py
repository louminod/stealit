from pynput import keyboard
import pytesseract
import pyperclip
import subprocess
from PIL import Image
import os

# cmd + shift + 0
COMBINATION = {keyboard.Key.cmd, keyboard.Key.shift, keyboard.KeyCode.from_char('0')}
current_keys = set()


def capture_screenshot():
    subprocess.run(["screencapture", "-i", "/tmp/screenshot.png"])
    screenshot = ""
    try:
        with open("/tmp/screenshot.png", "rb") as f:
            img = Image.open(f)
            screenshot = img.copy()
        img.close()
        os.remove("/tmp/screenshot.png")
    finally:
        return screenshot


def on_press(key):
    if key in COMBINATION:
        current_keys.add(key)

        if COMBINATION.issubset(current_keys):
            screenshot = capture_screenshot()
            if screenshot != "":
                text = pytesseract.image_to_string(screenshot)
                pyperclip.copy(text)


def on_release(key):
    try:
        current_keys.remove(key)
    except KeyError:
        pass


try:
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
except KeyboardInterrupt:
    pass
