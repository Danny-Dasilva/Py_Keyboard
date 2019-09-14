
from time import sleep
sleep(5)
class Write():
  def __init__(self, string):
    self.string = string
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
     
      if c == "'":
        write_report(NULL_CHAR*2+chr(52)+NULL_CHAR*5)

      if c == '"':
        write_report(chr(32)+NULL_CHAR+chr(52)+NULL_CHAR*5)
     


      write_report(NULL_CHAR*8)





# to do
# 54 , <
# 55 . >
# 56  / ?



class type:
  def __init__(self, string):
    self.string = string
  


Write.write('!@#$%^&*()[]"''":; = 123qwe')




# if c == 'a':
#         write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'A':
#         write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'b':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'B':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'c':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'C':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'd':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'D':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'e':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'E':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'f':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'F':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'g':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'G':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'e':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'E':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'f':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'F':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'g':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'G':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'h':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'H':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'i':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'I':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'j':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'J':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'k':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'B':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'b':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'B':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'b':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'B':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'b':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'B':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'b':
#         write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
#       if c == 'B':
#         write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)
#         write_report(NULL_CHAR*8)
      