s = 'c'
c = ord(s)
print(c)
import struct
string = 'Habclla TAst'
for c in string:
    if ord(c) > 96:
        s = ord(c) - 93
        write_report(NULL_CHAR*2+chr(s)+NULL_CHAR*5)
        write_report(NULL_CHAR*8)
    if ord(c) < 96:
        a = ord(c) - 61
        write_report(chr(32)+NULL_CHAR+chr(a)+NULL_CHAR*5)
        write_report(NULL_CHAR*8)


