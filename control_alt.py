from app.API import device

import time 


device.press('CTRL-ALT-T')

time.sleep(2)
device.press('CTRL-ALT-DELETE')
