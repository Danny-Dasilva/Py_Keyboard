NULL_CHAR = chr(0)


l = chr(32)+NULL_CHAR+chr(6)+NULL_CHAR*5


print(l.encode())

example = b'\x00\x00\x17\x00\x00\x00\x00\x00'

print(example.replace(b'\0', b''))
