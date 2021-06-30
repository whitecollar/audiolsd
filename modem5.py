import time
import serial

recipient = "89069749066"

phone = serial.Serial("/dev/ttyS1",  9600, timeout=5)
try:
    time.sleep(0.5)
    phone.write(b'ATZ\r')
    time.sleep(1)
    #phone.write(b'ATD"'+recipient.encode() +b'"\r')
    phone.write(b'ATD'+recipient.encode() +b';\r')
    while(1):
        print(phone.readline())
    time.sleep(0.5)
finally:
    phone.close()