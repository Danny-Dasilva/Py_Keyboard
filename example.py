
from app.HID import Keyboard
from app.HID import KeyboardLayoutUS
from time import sleep

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)


kbd.press("CONTROL ALT T")

layout.write('ls\n')

#todo 
keycodes = layout.keycodes('$')
print("done")