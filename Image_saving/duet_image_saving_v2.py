import os
#import traitlets
#import ipywidgets.widgets as widgets
#from IPython.display import display
#from jetbot import Camera, bgr8_to_jpeg
from uuid import uuid1
import time
import cv2


camera = cv2.VideoCapture(0)
camera.set(cv2.CAP_PROP_EXPOSURE, 30)

start = time.time()
for i in range(0,90):
    return_value, image = camera.read()

    #print(image.shape)
cv2.imwrite( str(uuid1()) + '.png', image)
end = time.time()
print(end-start)
del(camera)
