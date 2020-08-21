from ADC import Adc
from datetime import datetime
import urllib.request
import urllib.parse
import http.client
import json
from threading import Thread
import signal
import time

class Programa():
    def __init__(self):
        self.adc = Adc()
        self.time_in_milis = lambda: int(round(time.time() * 1000))
    
    def corriente_panel(self):  

        while True:

            self.adc.read();  

            if self.adc.cambio:
                print('Corriente ' + str(self.adc.corriente) )                

                url2='https://gensyslabs.net/agrega.php?corriente=%CORR&tiempo=%TIEM'.replace('%CORR', str(self.adc.corriente))
                url2=url2.replace('%TIEM', str(self.time_in_milis()))
                f = urllib.request.urlopen(url2,timeout=30)
                djson = json.loads(f.read())





programa = Programa()

subproceso_panel = Thread(target=programa.corriente_panel)
subproceso_panel.daemon = True
subproceso_panel.start()
signal.pause()    
