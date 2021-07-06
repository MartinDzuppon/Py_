import serial
import numpy as np

points=np.array([[1,1],[15,1], [15,15], [1,15], [1,1]])

 


serialPort = serial.Serial(port = "COM3", baudrate=57600,  bytesize=8, timeout=2, stopbits=serial.STOPBITS_TWO)

if not serialPort.isOpen():

    serialPort.open()


serialPort.write(b'!dim 1 1\r')   

N = points.shape[0]

for i in range(N):

    point = points[i]

    command = 'moa ' + str(point[0]) + ' ' + str(point[1]) + '\r'
    command_str = command.encode()
    type(command_str)
    serialPort.write(command_str)         #pohne stolik o 100 um v smere X aj Y

    c=0

serialString = ""                           # Used to hold data coming over UART

 
if not serialPort.isOpen():
    serialPort.open()

serialPort.write(b'!dim 1 1\r')             #nastavi jednotky vzdialenosti mikrony
serialPort.write(b'mor 10 10 \r')         #pohne stolik o 100 um v smere X aj Y

serialString = ""                           # Used to hold data coming over UART

serialPort.write(b'?pos\r')  
received = False
while(received==False):

    # Wait until there is data waiting in the serial buffer
    if(serialPort.in_waiting > 0):

        # Read data out of the buffer until a carraige return / new line is found
        serialString = serialPort.readline()
        positions = serialString.split()

        # Print the contents of the serial data
        print(serialString.decode('Ascii'))

        # Tell the device connected over the serial port that we recevied the data!
        # The b at the beginning is used to indicate bytes!
        received = True
        
serialPort.close()