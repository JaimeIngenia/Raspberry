import Adafruit_ADS1x15
from threading import Thread
import time


class Adc ():
    
    def __init__(self):
        self.corriente = 0
        self.prev_val = 0
        self.error = 100
        self.cambio = False
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.GAIN = 1
        
        #self.hilo = Thread(target=self.read)
        #self.hilo.daemon = True
        #self.hilo.start()
    
    def read(self):
        self.corriente = self.adc.read_adc(0,gain=self.GAIN)

        if self.corriente > (self.prev_val - self.error) and self.corriente < (self.prev_val + self.error):
            self.cambio = False        
        else:
            #print("Cambio")
            self.prev_val = self.corriente
            self.cambio = True
        time.sleep(.5)     
        #print(self.corriente)
         

if __name__=='__main__':
    adc = Adc()


    