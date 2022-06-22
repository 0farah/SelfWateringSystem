import RPi.GPIO as GPIO
import PCF8591 as pcf
import time
import bmp280 as b
import dhtt22 as d




relay=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay, GPIO.OUT)

pcf.setup(0x48)
sleepTime =1
try:
    while True:
        
        DH,T,H,P= d.humidite,d.temperature,pcf.read(1),b.hect
        print("Air Humidity is:",DH,"%")
        print("Humidity is: " , H,"%")
        print("temperature is: " , T, "C")
        print("Pressure is: " , P,"hPa")
        
        
        time.sleep(sleepTime)
        if(P>6)and(int(H)>60) and(T<37)and (DH<95):#condition d'arrosage
            print("il faut arroser")
            GPIO.output(relay, GPIO.HIGH)#ouvrir l'électrovanne
            time.sleep(5)#arroser pendant 5 sec
            GPIO.output(relay, GPIO.LOW)#fermer l'électrovanne
        else:
            print("il ne faut pas arroser")
            GPIO.output(relay, GPIO.LOW)
            
except KeyboardInterrupt:
    GPIO.output(relay, GPIO.LOW)
    GPIO.cleanup()