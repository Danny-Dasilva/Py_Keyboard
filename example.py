
from Py-Keyboard.HID import Keyboard, KeyboardLayoutUS
from time import sleep

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)


kbd.press("CONTROL ALT T")

layout.write('ls\n')

#todo 
keycodes = layout.keycodes('$')
print("done")