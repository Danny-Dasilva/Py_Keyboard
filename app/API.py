
from time import sleep

class device():
  def __init__(self, string):
    self.string = string
  def write_report(report):
      with open('/dev/hidg0', 'rb+') as fd:
          fd.write(report.encode())
  def write(string):
    #!/usr/bin/env python3
    NULL_CHAR = chr(0)

    def write_report(report):
        with open('/dev/hidg0', 'rb+') as fd:
            fd.write(report.encode())

    for c in string:
      #space
      if c == " ":
        write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)
      #lowercase
      if ord(c) > 96:
          s = ord(c) - 93
          write_report(NULL_CHAR*2+chr(s)+NULL_CHAR*5)
      #uppercasse
      if 64 < ord(c) < 91:
          a = ord(c) - 61
          write_report(chr(32)+NULL_CHAR+chr(a)+NULL_CHAR*5) 
      #numbers
      if 48 < ord(c) < 58:
          a = ord(c) - 19
          write_report(NULL_CHAR*2+chr(a)+NULL_CHAR*5)
      # 0 
      if ord(c) == 48:
          a = ord(c) - 9
          write_report(NULL_CHAR*2+chr(a)+NULL_CHAR*5)
     
      if c == '!':
        write_report(chr(32)+NULL_CHAR+chr(30)+NULL_CHAR*5)
     
      if c == '@':
        write_report(chr(32)+NULL_CHAR+chr(31)+NULL_CHAR*5)
     
      if c == '#':
        write_report(chr(32)+NULL_CHAR+chr(32)+NULL_CHAR*5)
   
      if c == '$':
        write_report(chr(32)+NULL_CHAR+chr(33)+NULL_CHAR*5)
  
      if c == '%':
        write_report(chr(32)+NULL_CHAR+chr(34)+NULL_CHAR*5)
  
      if c == '^':
        write_report(chr(32)+NULL_CHAR+chr(35)+NULL_CHAR*5)
       
      if c == '&':
        write_report(chr(32)+NULL_CHAR+chr(36)+NULL_CHAR*5)
      
      if c == '*':
        write_report(chr(32)+NULL_CHAR+chr(37)+NULL_CHAR*5)
       
      if c == '(':
        write_report(chr(32)+NULL_CHAR+chr(38)+NULL_CHAR*5)
      if c == ')':
        write_report(chr(32)+NULL_CHAR+chr(39)+NULL_CHAR*5)
      if c == '=':
        write_report(NULL_CHAR*2+chr(46)+NULL_CHAR*5)
      # if c == '{':
      #   write_report(chr(32)+NULL_CHAR+chr(47)+NULL_CHAR*5)
      if c == '[':
        write_report(NULL_CHAR*2+chr(47)+NULL_CHAR*5)
      # if c == '}':
      #   write_report(chr(32)+NULL_CHAR+chr(48)+NULL_CHAR*5)
      if c == ']':
        write_report(NULL_CHAR*2+chr(48)+NULL_CHAR*5)
      # if c == "\":
      #   write_report(chr(32)+NULL_CHAR+chr(47)+NULL_CHAR*5)
      # if c == '|':
      #   write_report(NULL_CHAR*2+chr(49)+NULL_CHAR*5)
      if c == ':':
        write_report(chr(32)+NULL_CHAR+chr(51)+NULL_CHAR*5)
      if c == ';':
        write_report(NULL_CHAR*2+chr(51)+NULL_CHAR*5)
     
      # if c == "'":
      #   write_report(NULL_CHAR*2+chr(52)+NULL_CHAR*5)

      if c == '"':
        write_report(chr(32)+NULL_CHAR+chr(52)+NULL_CHAR*5)
     


      write_report(NULL_CHAR*8)
    
  def press(string):
    #!there is a better wayto do this but im lazy
    NULL_CHAR = chr(0)
    def writer(input):
       with open('/dev/hidg0', 'rb+') as fd:
         fd.write(bytes(string))
    for word in string.split():
      if word == "ENTER":
        device.write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
      if word == "CTRL-ALT-T":
        with open('/dev/hidg0', 'rb+') as fd:
          fd.write(b'\x05\0\x17\0\0\0\0\0')
      if word == "CTRL-ALT-DELETE":
        with open('/dev/hidg0', 'rb+') as fd:
          fd.write(b'\x05\0\x4c\0\0\0\0\0')
        

      device.write_report(NULL_CHAR*8)





# to do
# 54 , <
# 55 . >
# 56  / ?

  



