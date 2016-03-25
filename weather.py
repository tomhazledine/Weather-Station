import json
import time
from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

# Attempt to get sensor reading.
    temp = sense.get_temperature()
    temp = round(temp, 1)
    humidity = sense.get_humidity()
    humidity = round(humidity, 1)
    pressure = sense.get_pressure()
    pressure = round(pressure, 1)

data = {
    'temp': temp,
    'humidity': humidity,
    'pressure': pressure
}

data['middle_name'] = 'Frederick';

print(json.dumps(data))


w = [255,255,255]
r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [159, 0, 255]
e = [0, 0, 0]

tick = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,b,
e,e,e,e,e,e,b,b,
e,b,e,e,e,b,b,e,
e,b,b,e,b,b,e,e,
e,e,b,b,b,e,e,e,
e,e,e,b,e,e,e,e,
e,e,e,e,e,e,e,e
]

sense.set_pixels(image)
time.sleep(.2)
sense.clear()

