#Import all the required libraries
import numpy as np
from imutils.contours import  sort_contours
import argparse
import imutils
import sys
import cv2

#Construct the argument parser and parse the arguments

ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
                help="Path of the image")
ap.add_argument("-r","--reference",type=str,
                default="ocr_a_reference.png",
                help="Path to reference OCR-A Image")
args = vars(ap.parse_args())

# define a dictionary that maps the first digit of a credit card
# number to the credit card type
FIRST_NUMBER = {"3": "American Express",
                "4": "Visa",
                "5": "MasterCard",
                "6": "Discover Card"
                }
#Load the OCR-A reference image from disk , convert it to a grayscale
#and threshold it such that digits appear as white on a black
#background

ref=  cv2.imread(args['reference'])
ref = cv2.cvtColor(ref,cv2.COLOR_BGR2GRAY)
ref =cv2.threshold(ref,10,255,cv2.THRESH_BINARY_INV)[1]
