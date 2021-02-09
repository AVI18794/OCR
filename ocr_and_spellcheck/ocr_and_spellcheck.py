#import all the required libraries
import pandas as pd
import numpy as np
import argparse
import cv2
from textblob import TextBlob
import pytesseract

#Create the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
                help="path to input image to be OCR'd")
args = vars(ap.parse_args())
# load the input image and convert it from BGR to RGB channel ordering
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# use Tesseract to OCR the image
text = pytesseract.image_to_string(rgb)
# show the text *before* ocr-spellchecking has been applied
print("BEFORE SPELLCHECK")
print("=================")
print(text)
print("\n")

#apply spell checking to the OCR'd text
tb = TextBlob(text)
corrected = tb.correct()

# show the text after ocr-spellchecking has been applied
print("AFTER SPELLCHECK")
print("================")
print(corrected)