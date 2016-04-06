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

image00 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

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
e,e,e,e,e,e,e,e
]

image3 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,w,e,e,e,e,
e,e,w,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

image4 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,w,e,e,e,
e,e,e,w,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]
image5 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

image6 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,o,r,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

image7 = [
e,e,e,e,e,e,e,e,
e,e,e,e,r,e,e,e,
e,e,e,r,o,r,e,e,
e,e,r,o,y,o,r,e,
e,e,e,r,o,r,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

image8 = [
e,e,e,e,r,e,e,e,
e,e,e,r,o,r,e,e,
e,e,r,o,y,o,r,e,
e,r,o,y,g,y,o,r,
e,e,r,o,y,o,r,e,
e,e,e,r,o,r,e,e,
e,e,e,e,r,e,e,e,
e,e,e,e,e,e,e,e
]

image9 = [
e,e,e,r,o,r,e,e,
e,e,r,o,y,o,r,e,
e,r,o,y,g,y,o,r,
r,o,y,g,b,g,y,o,
e,r,o,y,g,y,o,r,
e,e,r,o,y,o,r,e,
e,e,e,r,o,r,e,e,
e,e,e,e,r,e,e,e
]

image10 = [
e,e,r,o,y,o,r,e,
e,r,o,y,g,y,o,r,
r,o,y,g,b,g,y,o,
o,y,g,b,i,b,g,y,
r,o,y,g,b,g,y,o,
e,r,o,y,g,y,o,r,
e,e,r,o,y,o,r,e,
e,e,e,r,o,r,e,e
]

image11 = [
e,r,o,y,g,y,o,r,
r,o,y,g,b,g,y,o,
o,y,g,b,i,b,g,y,
y,g,b,i,v,i,b,g,
o,y,g,b,i,b,g,y,
r,o,y,g,b,g,y,o,
e,r,o,y,g,y,o,r,
e,e,r,o,y,o,r,e
]

image12 = [
r,o,y,g,b,g,y,o,
o,y,g,b,i,b,g,y,
y,g,b,i,v,i,b,g,
g,b,i,v,e,v,i,b,
y,g,b,i,v,i,b,g,
o,y,g,b,i,b,g,y,
r,o,y,g,b,g,y,o,
e,r,o,y,g,y,o,r
]

image13 = [
o,y,g,b,i,b,g,y,
y,g,b,i,v,i,b,g,
g,b,i,v,e,v,i,b,
b,i,v,e,e,e,v,i,
g,b,i,v,e,v,i,b,
y,g,b,i,v,i,b,g,
o,y,g,b,i,b,g,y,
r,o,y,g,b,g,y,o
]

image14 = [
y,g,b,i,v,i,b,g,
g,b,i,v,e,v,i,b,
b,i,v,e,e,e,v,i,
i,v,e,e,e,e,e,v,
b,i,v,e,e,e,v,i,
g,b,i,v,e,v,i,b,
y,g,b,i,v,i,b,g,
o,y,g,b,i,b,g,y
]

image15 = [
g,b,i,v,e,v,i,b,
b,i,v,e,e,e,v,i,
i,v,e,e,e,e,e,v,
v,e,e,e,e,e,e,e,
i,v,e,e,e,e,e,v,
b,i,v,e,e,e,v,i,
g,b,i,v,e,v,i,b,
y,g,b,i,v,i,b,g
]

image16 = [
b,i,v,e,e,e,v,i,
i,v,e,e,e,e,e,v,
v,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
v,e,e,e,e,e,e,e,
i,v,e,e,e,e,e,v,
b,i,v,e,e,e,v,i,
g,b,i,v,e,v,i,b
]

image17 = [
i,v,e,e,e,e,e,v,
v,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
v,e,e,e,e,e,e,e,
i,v,e,e,e,e,e,v,
b,i,v,e,e,e,v,i
]

image18 = [
v,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
v,e,e,e,e,e,e,e,
i,v,e,e,e,e,e,v
]

image19 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
v,e,e,e,e,e,e,e
]

image20 = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

images = [image00,image0,image1,image2,image3,image4,image5,image6,image7,image8,image9,image10,image11,image12,image13,image14,image15,image16,image17,image18,image19,image20]

while True:
    for image in images:
        sense.set_pixels(image)
        time.sleep(.05)
    time.sleep(1)