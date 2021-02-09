#import all the required files
import pandas as pd
import numpy as np
import argparse
import pytesseract
import cv2
import imutils



#Construct the argument parser and parse the arguments
ap  = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
                help="Path of the image to be OCR'd")

ap.add_argument("-d","--digits",type=int,default=1,
                help = "Whether or not *digits only* OCR will be performed")
args = vars(ap.parse_args())


#Load the image
image= cv2.imread(args['image'])
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
options = ""

if args['digits'] >0:
    options = "otuputbase digits"

text  = pytesseract.image_to_string(rgb ,config=options)
print(text)

