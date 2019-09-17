## Python Wrapper for emulkating a HID USB device for the raspi zero w

setup from  https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/

```python

from app.HID import Keyboard
from app.HID import KeyboardLayoutUS
from time import sleep

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)


kbd.press("CONTROL ALT T")

layout.write('ls\n')



```



## to do
add install.sh
keycodes = layout.keycodes('$')