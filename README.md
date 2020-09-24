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

### Editing 
All write operations are done inside the `send_report` function inside `Py_Keyboard>HID.py`

bytes written can be returned from the press and write function

```python


from Py_Keyboard.HID import Keyboard

kbd = Keyboard()

bytes_press = kbd.press("CONTROL ALT T")
print(bytes_press)
bytes_write = kbd.write('ls\n')
print(bytes_write)
```

### Keycodes
Keycodes are graciously borrowed from adafruit 

see documentation [here](Py_Keyboard/keycodes.py)


## to do

`keycodes = layout.keycodes('$')`

Test pip package import

