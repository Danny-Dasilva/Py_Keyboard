NULL_CHAR = chr(0)
t = chr(2)
print(t)

l = chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5


print(l.encode())

example = b'\x00\x05\x00\x00\x00\x00\x00'

print(example.replace(b'\0', b''))
