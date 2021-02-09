#Import all the required libraries
# import matplotlib.pyplot as plt
import argparse

# import textblob
import cv2
import pytesseract
from textblob import TextBlob

#Create the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i","--image",required=True,
                help="Path of the image to be OCR'd")
ap.add_argument("-l","--lang",type=str,default='es',
                help="language tp translate OCR'd  text to (default is English")
args = vars(ap.parse_args())

image = cv2.imread(args['image'])
rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)

#Use the tesseract to OCR the image , then replace newline characters
text = pytesseract.image_to_string(rgb)
text = text.replace("\n"," ")
#Show the original OCR'd text
print("ORIGINAL")
print("+++++++++++++")
print(text)
print("")
#Translate the text to a different language
tb = TextBlob(text)
translated = tb.translate(to=args['lang'])
#Show the translated text
print("TRANSLATED")
print("+++++++++++++++++")
print(translated)
