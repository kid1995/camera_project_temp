import os
import sys
from PIL import Image


#####################################################
# convert raw data
#####################################################
# require: installed imagemagick

print ("Enter number of frame, you want to convert: ")
num_pics = int(input())

command = "convert"
raw_img_postfix = ".raw"
bmp_img_postfix = ".bmp"
fileName = "image"
outputName = "image_out"
flags = ["-size 160x120", "-sampling-factor 4:2:2", "-depth 8"]
for i in range (1, num_pics):
    inputfile = "yuv:" + fileName + str(i) + raw_img_postfix
    outputFile = outputName +  str(i) + bmp_img_postfix

    os.system(command + " " + ' '.join(flags)+ " " + inputfile + " " + outputFile)
    print( inputfile + " => " + outputFile + " \n")
#####################################################
# Image open
#####################################################
    img = Image.open(outputFile)
    img.show()