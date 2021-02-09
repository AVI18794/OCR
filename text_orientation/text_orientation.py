#Import all the required libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import pytesseract
import cv2
import imutils
from pytesseract import Output



#Create the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
                help="Path of the image to be OCR'd")
args = vars(ap.parse_args())

#Load the input image
image = cv2.imread(args['image'])
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_osd(rgb,output_type = Output.DICT)

#Display the Orientation information
print("[INFO] detected orientation : {}".format(results['orientation']))
print("[INFO] rotate by {} degrees to correct".format(results['rotate']))
print("[INFO] detected script : {}".format(results['script']))

rotated = imutils.rotate_bound(image,angle=results['rotate'])

#Show the original image and image after orientation
#corrected
cv2.imshow("Original",image)
cv2.imshow("Output",rotated)
cv2.waitKey(0)
cv2.destroyAllWindows()
