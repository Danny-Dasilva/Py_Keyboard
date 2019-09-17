
from app.ada_hid import Keyboard
from app.ada_hid import KeyboardLayoutUS
import time
time.sleep(2)
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)

# Type 'abc' followed by Enter (a newline).
layout.write('hello is this working\n')

# Get the keycodes needed to type a '$'.
# The method will return (Keycode.SHIFT, Keycode.FOUR).
keycodes = layout.keycodes('$')