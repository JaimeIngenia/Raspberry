import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2

while True:

    value = adc.read_adc_difference(0, gain=GAIN)
    print('Channel 0 minus 1: {0}'.format(value))
    time.sleep(0.5)