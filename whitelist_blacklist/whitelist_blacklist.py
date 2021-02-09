#Import all the required libraries
import pandas as pd
import numpy as np
import cv2
import argparse
import pytesseract
import imutils

#Construct the argument parser and parse the arguments
ap  = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
                help="Path of the image to be OCR'd ")
ap.add_argument("-w","--whitelist",type=str,default="",
                help="list of characters to whitelist")
ap.add_argument("-b","--blacklist",type=str,default="",
                help="list of characters to blacklist")

args = vars(ap.parse_args())


#Load the image
image = cv2.imread(args['image'])
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
options = ""

#Check to see if a set of whitelist characters has been
# provided and if so , update our options string
if len(args['whitelist']) >0:
    options+= "-c tessedit_char_whitelist={}".format(args['whitelist'])

#Check to see if a set of blacklist characters has been
#provided and if so,update our options string
if len(args['blacklist']) >0:
    options += "-c tessedit_char_blacklist={}".format(args['blacklist'])


#OCR the input image using Tesseract
text  = pytesseract.image_to_string(rgb,config=options)
print(text)


