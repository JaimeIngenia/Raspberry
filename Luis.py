import time

import Adafruit_ADS1x15


adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
adc.start_adc_comparator(0,  # Channel number
                         20000, 5000,  # High threshold value, low threshold value
                         active_low=True, traditional=True, latching=False,
                         num_readings=1, gain=GAIN)
print('Reading ADS1x15 channel 0 for 10 seconds with comparator...')
start = time.time()
while (time.time() - start) <= 10.0:
    
    value = adc.get_last_result()

    print('Channel 0: {0}'.format(value))

    time.sleep(0.5)

adc.stop_adc()