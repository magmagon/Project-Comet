import os
import cv2
import os
from typing import List #File operations
import cv2 #Image Manipulation
import csv #Data logging
import numpy as np #Array operations
from PIL import Image #Image Operations

#image = cv2.imread()
#ingest_dir = 'C:/Users/Magmagon/Pictures/Project-Comet-main/ProjectComet/ingest/'
#output_dir = 'C:/Users/seagu/Pictures/ProjectComet/temporary/'
#readFileNameList = os.listdir(input_dir)
#print(readFileNameList)


current_dir = os.getcwd()
input_dir = current_dir + "/ingest/"
output_dir = current_dir + '/temporary/'

count = 0

width_dimension = 4000
height_dimension = 3000
resize_dimension = (width_dimension, height_dimension)

#img = cv2.imread("C:/Users/seagu/Pictures/ProjectComet/ingest/112082unimgNoise70.jpg")
#cv2.imshow("image",img)
#cv2.waitKey()

'''
for eachFile in FileNameList:
    print(eachFile)
    img = cv2.imread(eachFile)
    
#    cv2.imwrite(output_dir + str(eachFile) + "resized.jpg", resized_image)

    resized_image = cv2.resize(img, resize_dimension, interpolation = cv2.INTER_LINEAR)
#    cv2.imwrite(output_dir + str(eachFile) + "edge.jpg", resized_image)
    edges = cv2.Canny(resized_image, 10,100)
#    cv2.imshow("image", resized_image)
#    cv2.imshow("edge", edges)
#    cv2.waitKey()
    output_dir += str(eachFile)
#    print(output_dir)
    cv2.imwrite(output_dir + str(eachFile) + "edge.jpg", edges)
'''



#This is the unifed code of imageprocessor.py, split.py, and colorcode.py

###Section 1: Imageprocessor - Imports image and resizes it to 4000x3000 pixels, then turns each picture to gray scale, then runs the canny edge filter

def image_importer(input_dir):
    os.chdir(input_dir)
    List_of_Files = os.listdir(input_dir)
    print(List_of_Files)
    for file in List_of_Files:
        try:
            originalImg = cv2.imread(file)
            image_resize(originalImg)
            print("success 1")
        except ValueError:
            print("File format not valid")

def image_resize(image):
    width_dimension = 4000
    height_dimension = 3000
    resize_dimension = (width_dimension, height_dimension)
    resized_image = cv2.resize(image, resize_dimension, interpolation = cv2.INTER_LINEAR_EXACT)
    edge_filter(resized_image)
    print("success 2")

def edge_filter(image):
    edges = cv2.Canny(image, 10,100)
    os.chdir(output_dir)
    cv2.imwrite(output_dir + "EDGE.jpg", edges)
    if not cv2.imwrite(output_dir + "EDGE.jpg", edges):
        raise Exception("no work")
    print(os.getcwd())
    print(os.listdir(output_dir))
    


'''
minval = [150,200,300]
maxval = [300,400,400]
img = cv2.imread(FileNameList[0])
#edges = cv2.Canny(img, 200, 400)
#cv2.imwrite(output_dir + "new.jpg", img)

for x in range(len(minval)):
    edges = cv2.Canny(img, minval[x], maxval[x])
    cv2.imwrite(output_dir + str(x) + "edge.jpg", edges)
    print(minval[x], maxval[x])
'''