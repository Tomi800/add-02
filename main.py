from machine import ADC
from machine import Pin
import time

adc = ADC(26)
nashe = adc.read_u16()

VD = 3.3 / (65535)

while True:
    ReglaTres = nashe * VD
    temperatura = ReglaTres/0.01
    
    print ("El voltaje es: %.2f" %ReglaTres)
    print ("La temperatua es: %.2f" %temperatura)
    
    time.sleep(1)
