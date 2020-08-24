from base import Adc
from threading import Thread               
import signal                              
import time

while True:
    adc = Adc()
    adc.read(); 
    if  adc.Ieficaz > (adc.prev_val - adc.error) and adc.Ieficaz< (adc.prev_val + adc.error):
        adc.cambio = False    
        print("NO Cambio")
    else:
        print("Cambio")
        adc.prev_val = adc.Ieficaz
        adc.cambio = True    
        print('Corriente ' + str(adc.Ieficaz) + ' pre ' + str(adc.prev_val) ) 
        print('Potencia ' + str(adc.potencia) ) 
    del adc
    time.sleep(0.5)