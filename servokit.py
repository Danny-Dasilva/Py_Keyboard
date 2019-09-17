
from app.ada_hid2 import Keyboard
from app.ada_hid2 import KeyboardLayoutUS
from app.keycode import Keycode
import time
time.sleep(2)
kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)



#layout.write('abc\n')
# Type 'abc' followed by Enter (a newline).

# kbd.release_all()
# kbd.press(Keycode.CONTROL, Keycode.ALT, Keycode.T,)
# kbd.release_all()
kbd.press("CONTROL ALT T")
kbd.release_all()

# Get the keycodes needed to type a '$'.
# The method will return (Keycode.SHIFT, Keycode.FOUR).
keycodes = layout.keycodes('$')
print("done")