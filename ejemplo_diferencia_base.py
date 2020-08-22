import time
import Adafruit_ADS1x15
import math

GAIN = 2
def med_Ieficaz():
    sumIinstant=0
    for i in range(1,10):
        bitsads=adc.read_adc_difference(0, gain=GAIN)
        mVinstant = bitsads * 0.625
        Iinstant = mVinstant * 10 / 1000 
        sumIinstant = sumIinstant + pow((Iinstant),2)
    res=sumIinstant/10
    Ieficaz = math.sqrt(res) 
    return (Ieficaz)

while True:
    adc = Adafruit_ADS1x15.ADS1115()
    value=med_Ieficaz()
    print('Channel 0 minus 1: {0}'.format(value))