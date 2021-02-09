#import all the required files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import argparse
import pytesseract
import cv2

#Create the argument parser
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,help="Path of the image to be OCR'd")
args = vars(ap.parse_args())

#Load the image
image = cv2.imread(args['image'])
image = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

text = pytesseract.image_to_string(image)
print(text)

