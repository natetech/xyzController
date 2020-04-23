# Make a module 
'''
gcode flavor: 
Duet gcode 
'''
import serial
import time 

MESSAGE = ''

ser = serial.Serial(port='/dev/ttyACM0',baudrate=115200)

#   get_image_matrix( 5,  7,   53,   25)
def get_image_matrix(nX, nY, xSep, ySep):
    offsetX = 0
    offsetY = 0
    # Save image location as nXxnY, like customName_sheetName_1x1.jpg
    for xDevice in range(1,nX+1):
        for yDevice in range(1,nY+1):
            # Start with the first device 
            MESSAGE = 'G0 X{} Y{} F6000\r\n'.format( offsetX+(xDevice*xSep), offsetY+(yDevice*ySep)).encode('utf-8')
            ser.write(MESSAGE)
            #    print('G0 X{} Y{} F6000\r\n'.format( offsetX+(xDevice*xSep), offsetY+(yDevice*ySep)))
            time.sleep(3)
    # Return to origin: 
    MESSAGE = 'G0 X{} Y{} F6000\r\n'.format( offsetX, offsetY).encode('utf-8')
    ser.write(MESSAGE)
            
get_image_matrix(5, 7, 53, 25)

ser.close()