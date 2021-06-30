"""\
Demo: dial a number (simple example using polling to check call status)

Simple demo app that makes a voice call and plays sone DTMF tones (if supported by modem)
when the call is answered, and hangs up the call.
It polls the call status to see if the call has been answered

Note: you need to modify the NUMBER variable for this to work
"""

from __future__ import print_function

import sys, time, logging

PORT = '/dev/ttyS1'
BAUDRATE = 9600
NUMBER = '89069749066' # Number to dial - CHANGE THIS TO A REAL NUMBER
PIN = None # SIM card PIN (if any)

from gsmmodem.modem import GsmModem
from gsmmodem.exceptions import InterruptedException, CommandError
 
def main():
    print('Initializing modem...')
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
    modem = GsmModem(PORT, BAUDRATE)
    modem.connect(PIN)
    print('Waiting for network coverage...')
    modem.waitForNetworkCoverage(30)
    print('Dialing number: {0}'.format(NUMBER))
    call = modem.dial(NUMBER)
 
    i = 0
    while i < 1000:
        print('Checking internal call status:')
        modem.write('AT+CLCC')
        if not call.active:
            print('Call object no longer active, exiting...')
            i = 999999
        else:
            time.sleep(0.5)
    print('Done.')
    modem.close()
 
if __name__ == '__main__':
    main()