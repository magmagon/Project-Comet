import os
from typing import List #File operations
import cv2 #Image Manipulation
import csv #Data logging
import numpy as np #Array operations
from PIL import Image #Image Operations

#This is the unifed code of imageprocessor.py, split.py, and colorcode.py

###Section 1: Imageprocessor - Imports image and resizes it to 4000x3000 pixels, then turns each picture to gray scale, then runs the canny edge filter

input_dir = 'C:/Users/seagu/Pictures/ProjectComet/ingest/'
output_dir = 'C:/Users/seagu/Pictures/ProjectComet/temporary/'

def image_importer(input_dir):
    List_of_Files = os.listdir("c:/users/seagu/pictures/projectcomet/ingest")
    print(List_of_Files)
    for file in List_of_Files:
        try:
            originalImg = cv2.imread(file)
            print("success 1")
            image_resize(originalImg)
        except ValueError:
            print("File format not valid")

def image_resize(image):
    width_dimension = 4000
    height_dimension = 3000
    resize_dimension = (width_dimension, height_dimension)
    resized_image = cv2.resize(image, resize_dimension, interpolation = cv2.INTER_LINEAR_EXACT)
    print("success 2")
    edge_filter(resized_image)

def edge_filter(image):
    edges = cv2.Canny(image, 10,100)
    cv2.imwrite(output_dir + str(image) + "EDGE.jpg", edges)
    print("success 3")
    processed_image_importer("c:/users/seagu/pictures/projectcomet/temporary")

###Section 2: Split - Divides image into 100x100 pixel squares and then analyzes the ratio of edges in the picture and sends results to csv or text file
input_dir = "C:/Users/seagu/Pictures/ProjectComet/temporary/"
output_dir = "C:/Users/seagu/Pictures/ProjectComet/temporary/chunks/"


def processed_image_importer(input_dir):
    List_of_Files = os.listdir(input_dir)
    print(List_of_Files, input_dir)
    for File in List_of_Files:
        image = cv2.imread(File)
        dimensions = image.shape
        x_split = int(dimensions[1]/40)
        y_split = int(dimensions[0]/30)
        print("success 4")
        splitter(image, x_split, y_split)
        
def splitter(image, x_split, y_split):
    ratio_list = []
    x_pixel = 0
    y_pixel = 0 
    for x_iteration in range(40):
        for y_iteration in range(30):
            split_image = image[y_pixel:y_pixel + y_split,x_pixel:x_pixel+x_split]
            white_pixels = int(np.sum(split_image >= 200))
            black_pixels = int(np.sum(split_image <= 100))
            ratio = (1000 * white_pixels / (black_pixels + 1))
            ratio_list.append(ratio)
            print("x,y", x_pixel, y_pixel)
  
            #print("iteration", x_iteration, y_iteration)
            #cv2.imwrite(output_dir + str(x_iteration + y_iteration) + ".jpg", split_image)
            y_pixel += y_split

        x_pixel += x_split
        y_pixel = 0
    print("success 5")
    datawrite(ratio_list)
    equalizer(ratio_list)   

def datawrite(ratio_list):
    with open("c:/users/seagu/pictures/projectcomet/output/ratios.csv", 'w', newline = '') as outputfile:
        writer = csv.writer(outputfile)
        for item in ratio_list:
            write = [item]
            writer.writerow(write)
        np.savetxt("c:/users/seagu/pictures/projectcomet/output/ratios.txt", ratio_list, fmt ='%s')
    print("success 5")
    
###Section 3: Uses ratio list from section 2 to compile back into image gradient to overlay on top of original file
def file_importer(): #Only use this if you already have a list of values to compile
    with open("C:/Users/seagu/Pictures/ProjectComet/output/split.csv", 'r') as inputFile:
        reader = csv.reader(inputFile, delimiter=',')
        ratios = []

        for item in reader:
            ratios.append(float(item[0]))

def equalizer(ratio_list):
    minimumChonk = min(ratio_list)
    maximumChonk = max(ratio_list)
    spectrum = 255 / (maximumChonk - minimumChonk)
    for count in range(len(ratio_list)):
        ratio_list[count] *= spectrum
    print("success 6")


def rebuilder(ratio_list):
    grid = np.array(ratio_list)
    grid2 = np.reshape(grid, (40,30))
    colorImage = Image.fromarray(grid2)
    colorImage = colorImage.convert("L")
    colorImage.save("C:/Users/seagu/Pictures/ProjectComet/output/color.png")
    output = colorImage.resize((4000,3000))
    output.save('C:/Users/seagu/Pictures/ProjectComet/output/upscaled.png')

image_importer(input_dir)