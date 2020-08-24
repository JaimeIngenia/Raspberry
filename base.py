import time
import Adafruit_ADS1x15
import math

class Adc ():
    
    def __init__(self):
        self.GAIN = 2
        self.adc = Adafruit_ADS1x15.ADS1115()
        self.bitsads=0
        self.mVinstant=0
        self.Iinstant=0
        self.sumIinstant=0
        self.res=0
        self.Ieficaz=0
        self.prev_val = 0
        self.error = 0.1
        self.cambio = False
        self.potencia=0

    def read(self):
        self.sumIinstant=0
        for i in range(1,200):
            self.bitsads = self.adc.read_adc_difference(0, gain=self.GAIN)
            self.mVinstant = self.bitsads * 0.625
            self.Iinstant = self.mVinstant * 10 / 1000 
            self.sumIinstant = self.sumIinstant + pow((self.Iinstant),2)
        self.res=self.sumIinstant/200
        self.Ieficaz = (math.sqrt(self.res) )*0.4
        self.potencia=self.Ieficaz*220

if __name__=='__main__':
    adc = Adc()



