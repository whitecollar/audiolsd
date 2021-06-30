from __future__ import print_function                                                                            
                                                                                                                 
import sys, time, logging                                                                                        
                                                                                                                 
PORT = '/dev/ttyS1'                                                                                              
BAUDRATE = 9600                                                                                                  
NUMBER = '89069749066' # Number to dial - CHANGE THIS TO A REAL NUMBER                                           
PIN = None # SIM card PIN (if any)                                                                               
                                                                                                                 
from gsmmodem.modem import GsmModem                                                                              
#from gsmmodem.exceptions import InterruptedException, CommandError                                              
                                                                                                                 
#waitForCallback = True                                                                                          
                                                                                                                 
                                                                                                                 
def main():                                                                                                      
    if NUMBER == None or NUMBER == '00000':                                                                      
        print('Error: Please change the NUMBER variable\'s value before running this example.')                  
        sys.exit(1)                                                                                              
    print('Initializing modem...')                                                                               
    logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)                                
    modem = GsmModem(PORT, BAUDRATE)                                                                             
    modem.connect(PIN)                                                                                           
    print('Waiting for network coverage...')                                                                     
    modem.waitForNetworkCoverage(30)  
    #logging.info("Loading %s with %s", unit, cardcode)
    call = modem.dial(NUMBER)

    wasAnswered = False

    while call.active:
      if call.answered:
        wasAnswered = True
        logging.info("Call answered")
        time.sleep(10.0)
        if call.active:
          logging.info("Hanging up")
          call.hangup()
        else:
          logging.info("Call ended by remote party")
      else:
        time.sleep(0.5)


                                                                                           
                                                                                                                 
if __name__ == '__main__':                                                                                       
    main()