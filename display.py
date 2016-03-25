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

image0 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

image1 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

image2 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

image3 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,w,e,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

image4 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,w,e,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

image5 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,g,r,e,e,
e,e,e,w,r,e,e,e,
e,e,w,e,e,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

image6 = [
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,g,r,e,e,
e,e,r,g,b,g,r,e,
e,e,e,r,g,r,e,e,
e,e,w,e,r,e,e,e,
e,w,e,e,e,e,e,e,
w,e,e,e,e,e,e,e
]

images = [image0,image1,image2,image3,image4,image5,image6]

while True:
    for image in images:
        sense.set_pixels(image)
        time.sleep(1)