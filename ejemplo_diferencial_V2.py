import time
import Adafruit_ADS1x15
import math

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2

def med_Ieficaz():
    sumIinstant=0
    for i in range(1,200):
        bitsads=adc.read_adc_difference(0, gain=GAIN)
        mVinstant = bitsads * 0.625
        Iinstant = mVinstant * 10 / 1000 
        sumIinstant = sumIinstant + pow((Iinstant),2)
    res=sumIinstant/200
    Ieficaz = math.sqrt(res) 
    return (Ieficaz)

while True:
    Int_calculada = med_Ieficaz() * 1.409
    #print (Int_calculada)
    time.sleep(0.5)

