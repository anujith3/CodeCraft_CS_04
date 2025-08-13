# Keystroke Logger using `pynput`

This Python script logs keyboard inputs using the `pynput` library. It captures each key press and writes it to a file named `keylog.txt` in the same directory.

## How It Works

- Regular keys (letters, numbers, symbols) are logged as they are typed.
- Special keys (e.g., `Enter`, `Shift`, `Backspace`, `Space`, etc.) are recorded in square brackets, like `[enter]`, `[space]`.
- Pressing the `Esc` key stops the keylogger.

## Requirements

Install the required Python package:

```bash
pip install pynput
