import os
import traitlets
#import ipywidgets.widgets as widgets
#from IPython.display import display
#from jetbot import Camera, bgr8_to_jpeg
from uuid import uuid1

from jetcam.usb_camera import USBCamera
from jetcam.utils import bgr8_to_jpeg

directory = '.'


# Start the camera and create a video stream 
#camera = USBCamera(capture_device=1)
camera = USBCamera(width=224, height=224, capture_width=640, capture_height=480, capture_device=0)
print(camera.value.shape)

# Get an bgr8 image from the camera
image = camera.read()
print(camera.value.shape)
toJpeg = bgr8_to_jpeg(image)

image_path = os.path.join(directory, str(uuid1()) + '.jpg')

with open(image_path, 'wb') as f:
    f.write(image.value)
