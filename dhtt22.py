import Adafruit_DHT 
import time
print ('Start')

humidite,temperature=Adafruit_DHT.read(Adafruit_DHT.DHT22,25)
"""while True:

    if humidite is not None and temperature is not None:
        print('Température={0:0.1f}*Humidité={1:0.1f}%'.format(temperature,humidite))
    else:
        print('Echec de lecture du capteur!')
    time.sleep(2)"""