from datetime import datetime
import urllib.request
import urllib.parse
import http.client
import json

import time
import Adafruit_ADS1x15

now = datetime.now()

adc = Adafruit_ADS1x15.ADS1115()
GAIN = 1
adc.start_adc_comparator(0,  # Channel number
                         20000, 5000,  # High threshold value, low threshold value
                         active_low=True, traditional=True, latching=False,
                         num_readings=1, gain=GAIN)
print('Reading ADS1x15 channel 0 for 10 seconds with comparator...')
start = time.time()

link = 'https://gensyslabs.net/agrega.php'
inicio ='?corriente='
intermedio = '&tiempo='



while (time.time() - start) <= 10.0:
    
    value = adc.get_last_result()
    url2=('https://gensyslabs.net/agrega.php?corriente={0}'.format(value)) + intermedio 
    f = urllib.request.urlopen(url2,timeout=30)
    djson = json.loads(f.read())
    print(djson)
    print(url2)

    time.sleep(0.5)

adc.stop_adc()