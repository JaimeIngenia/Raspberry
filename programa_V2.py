from base import Adc
from threading import Thread               
import signal                              
import time
from datetime import datetime
import urllib.request
import urllib.parse
import http.client
import json

adc = Adc()
while True:
    adc.read(); 
    #print('pre val ' + str(adc.prev_val) )
    #print('error ' + str(adc.error) )
    if  abs(adc.Ieficaz - adc.prev_val) > adc.error:
        #print("Cambio")
        adc.prev_val = adc.Ieficaz
        adc.cambio = True    
        print('Corr' + str(adc.Ieficaz) )
        print('cal-error ' +str(abs(adc.Ieficaz - adc.prev_val)) )
        
        url2='https://gensyslabs.net/agrega.php?corriente=%CORR'.replace('%CORR', str(adc.Ieficaz))
        #url2=url2.replace('%TIEM', str(1))
        print(url2)
        f = urllib.request.urlopen(url2,timeout=30)
        djson = json.loads(f.read())


    else:
        adc.cambio = False    
        #print("NO Cambio")
    #print('Corriente ' + str(adc.Ieficaz) + ' pre ' + str(adc.prev_val) ) 
    #print('Potencia ' + str(adc.potencia) ) 
    time.sleep(0.5)