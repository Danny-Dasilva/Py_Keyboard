
from time import sleep
class Press():
  def __init__(self, string):
    self.string = string
  def test(string):
    #!/usr/bin/env python3
    NULL_CHAR = chr(0)

    def write_report(report):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(report.encode())

    for c in string:
      print(c)
      if c == 'a':
        write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
        sleep(.05)
        write_report(NULL_CHAR*8)
    

class type:
  def __init__(self, string):
    self.string = string
  


Press.test('Halla Tast')

