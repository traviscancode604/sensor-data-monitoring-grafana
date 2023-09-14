# this file is meant for testing if the sensor data is being captured
# it will print the current humidity and temperature to the console at a 30 sec interval
# remember to wire the data output of the sensor, to the gpio pin 4 in the raspberry pi

import Adafruit_DHT as dht_sensor
import time

def get_temperature_readings():
    humidity, temperature = dht_sensor.read_retry(dht_sensor.DHT22, 4) # gpio pin 4 data out
    humidity = format(humidity, ".2f") + "%"
    temperature = format(temperature, ".2f") + "C"
    return {"temperature": temperature, "humidity": humidity}

while True:
    print(get_temperature_readings())
    time.sleep(30)
