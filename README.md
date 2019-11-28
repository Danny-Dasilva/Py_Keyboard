## Python HID USB emulator

Python Wrapper for emulating a HID USB device for the raspi zero w

setup from  https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/



## git repo

`pip3 install git+https://github.com/Danny-Dasilva/Py_Keyboard.git`
## on a brand new pi zero w


`git clone https://github.com/Danny-Dasilva/Py_Keyboard.git`

in Py_Keyboard folder

`source install.sh`


example.py


```python



from Py_Keyboard.HID import Keyboard

kbd = Keyboard()

kbd.press("CONTROL ALT T")

kbd.write('ls\n')







```



## to do

`keycodes = layout.keycodes('$')`

Test pip package import

