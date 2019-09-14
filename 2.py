
import struct
string = '0123456789ABCDabcdzzZZ'
for c in string:
    #lowercase
    if ord(c) > 96:
        s = ord(c) - 93
    #uppercasse
    if 64 < ord(c) < 91:
        a = ord(c) - 61
        
    #numbers
    if 48 < ord(c) < 58:
        a = ord(c) - 19
    # 0 
    if ord(c) == 48:
        a = ord(c) - 9