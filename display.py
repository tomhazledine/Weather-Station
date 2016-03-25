from sense_hat import SenseHat
import time

sense = SenseHat()

w = [255,255,255]
r = [255, 0, 0]
o = [255, 127, 0]
y = [255, 255, 0]
g = [0, 255, 0]
b = [0, 0, 255]
i = [75, 0, 130]
v = [159, 0, 255]
e = [0, 0, 0]  # e stands for empty/black

images[0] = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

images[1] = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

images[2] = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

images[3] = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,w,e,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

images[4] = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,w,e,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

images[5] = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,g,r,e,e,
e,e,e,w,r,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

images[5] = [
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,g,r,e,e,
e,e,r,g,b,g,r,e,
e,e,e,r,g,r,e,e,
e,e,w,e,r,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

white True:
    for image in images:
        sense.set_pixels(image)
        time.sleep(1)