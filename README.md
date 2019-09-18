## Python Wrapper for emulkating a HID USB device for the raspi zero w

setup from  https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/



## git repo

`pip3 install git+https://github.com/Danny-Dasilva/Py-Keyboard.git`
## on a brand new pi zero w

run

`source install.sh`



```python


from app.HID import Keyboard, KeyboardLayoutUS
from time import sleep

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)


kbd.press("CONTROL ALT T")

layout.write('ls\n')





```



## to do
add install.sh
keycodes = layout.keycodes('$')