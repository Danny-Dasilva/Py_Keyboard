## Python Wrapper for emulkating a HID USB device for the raspi zero w

setup from  https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/



## git repo

`pip3 install git+https://github.com/Danny-Dasilva/Py_Keyboard.git`
## on a brand new pi zero w

run

`source install.sh`



```python


from Py_Keyboard.HID import Keyboard, KeyboardLayoutUS

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)


kbd.press("CONTROL ALT T")

layout.write('ls\n')





```



## to do

`keycodes = layout.keycodes('$')`
