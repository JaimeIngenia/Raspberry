import time
import Adafruit_ADS1X15
import math

adc = Adafruit_ADS1x15.ADS1115()
GAIN =1

print('Press Ctrl-C to quit...')
while True:

    mVporbit = 0.0625
    sumIinstant=0
    for i in range(1,200):
        bitsads=adc.read_adc_difference(0, gain=GAIN)
        mVinstant = bitsads * mVporbit
        Iinstant = mVinstant * 10 / 1000
        sumIinstant += pow((Iinstant),2)

    Ieficaz = math.sqrt(sumIinstant / 200)
    print('Channel 0 minus 1: {0}'.format(Ieficaz))
    
    time.sleep(0.5)