import time
import Adafruit_ADS1x15
from threading import Thread
import math

adc = Adafruit_ADS1x15.ADS1115()
GAIN =1

while True:
    mVporbit = 0.0625
    sumIinstant=0
    for i in range(1,200):
        bitsads=adc.read_adc_difference(0, gain=GAIN)
        mVinstant = bitsads * mVporbit
        Iinstant = mVinstant * 10 / 1000 
        sumIinstant = sumIinstant + pow((Iinstant),2)
    #value = adc.read_adc_difference(0, gain=GAIN)
    res=sumIinstant/200
    Ieficaz = (math.sqrt(res))
    potencia=Ieficaz* 220
    #print('Corriente Instantanea: {0} A'.format(Ieficaz))
    #print('Potencia Instantanea: {0} W'.format(potencia))
    
    time.sleep(0.5)