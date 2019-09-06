import serial
import os
import serial.tools.list_ports
import sys
from PIL import Image

#####################################################
# connect to serial port
#####################################################
if os.name=='posix':
    ser = serial.Serial('/dev/ttyUSB0')
elif os.name=='nt':
    print("choose device index:")
    comlist = serial.tools.list_ports.comports()
    for i, elem in enumerate(comlist):
        print(str(i) + ":" + elem.device)
        sys.stdout.flush()
    idx = int(input())
    ser = serial.Serial(comlist[idx].device, 115200)

#####################################################
# port config
#####################################################
ser.baudrate=115200
ser.bytesize=8
ser.parity='N'
print("open " + ser.name + "\nbaud: " + str(ser.baudrate) + "\ndata format:" + str(ser.bytesize) + str(ser.parity) + str(ser.stopbits))


#####################################################
# prepare file
#####################################################

#####################################################
# pic format config
#####################################################
picSize160x120=38400
picSize = picSize160x120

raw_img_postfix = ".raw"
data_buffer = []

print ("Enter number of frame, you want to convert: ")
num_pics = int(input())

for i in range (1,num_pics):
#####################################################
# get data from uart-usb
#####################################################
    print("reading data...")
    picData = []
    for pixel in range(picSize):
        bit = ser.read()
        picData.append(bit)
    data_buffer.append(picData)

    print('\n'+'Total size: '+str(len(picData)) + ' bytes')

count = 0
for data in data_buffer:
    fileName = "image"
    count +=1;
    fileName = fileName + str(count) + raw_img_postfix
    fileRaw = open(fileName, "wb+")
    for bit in data:
        fileRaw.write(bit)
    fileRaw.close()
#####################################################
# convert raw data
#####################################################
# require: installed imagemagick
#command = "convert"
#flags = ["-size 160x120", "-sampling-factor 4:2:2", "-depth 8"]
#inputFormat = "yuv:" + fileName
#outputFile = "image_out.bmp"

#os.system(command + " " + ' '.join(flags)+ " " + inputFormat + " " + outputFile)

#####################################################
# Image open
#####################################################
#img = Image.open('image_out.bmp')
#img.show()

