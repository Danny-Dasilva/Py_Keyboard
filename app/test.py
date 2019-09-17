
import time
def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

shift_cmd_5 = "5\x0\x4c\x0\x0\x0\x0\x0"
write_report(shift_cmd_5)
print("SNAP!!")
time.sleep(0.2)
write_report("\x0\x0\x0\x0\x0\x0\x0\x0")
