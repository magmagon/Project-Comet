import os
from typing import List #File operations
import cv2 #Image Manipulation
import csv #Data logging
import numpy as np #Array operations
from PIL import Image #Image Operations

#This is the unifed code of imageprocessor.py, split.py, and colorcode.py

###Section 1: Imageprocessor - Imports image and resizes it to 4000x3000 pixels, then turns each picture to gray scale, then runs the canny edge filter

current_dir = os.getcwd()
input_dir = current_dir + "/ingest/"
temporary_dir = current_dir + '/temporary/'
output_dir = current_dir + "/output/"

#IMPORT SECTION#

os.chdir(input_dir)
List_of_Files = os.listdir(input_dir)
for file in List_of_Files:
    try:
        originalImg = cv2.imread(file)
        print("success 1")
    except ValueError:
        print("File format not valid")
    
width_dimension = 4000
height_dimension = 3000
resize_dimension = (width_dimension, height_dimension)
resized_image = cv2.resize(originalImg, resize_dimension, interpolation = cv2.INTER_LINEAR_EXACT)

edges = cv2.Canny(resized_image, 10,100)
output_file = output_dir + 'temporary.png'
print(output_file)
cv2.imwrite(output_file, edges)

dimensions = edges.shape
x_split = int(dimensions[1]/400)
y_split = int(dimensions[0]/300)
print("success 4")

#ANALYSIS SECTION#

ratio_list = []
x_pixel = 0
y_pixel = 0 
for x_iteration in range(400):
    for y_iteration in range(300):
        split_image = edges[y_pixel:y_pixel + y_split,x_pixel:x_pixel+x_split]
        white_pixels = int(np.sum(split_image >= 200))
        black_pixels = int(np.sum(split_image <= 100))
        ratio = (1000 * white_pixels / (black_pixels + 1))
        ratio_list.append(ratio)
        #print("x,y", x_pixel, y_pixel)
  
        #print("iteration", x_iteration, y_iteration)
        #cv2.imwrite(output_dir + str(x_iteration + y_iteration) + ".jpg", split_image)
        y_pixel += y_split

    x_pixel += x_split
    y_pixel = 0
    
print("success 5")

ratio_csv = output_dir + "ratios.csv"
ratio_text = output_dir + "ratios.txt"

with open(ratio_text, 'w', newline = '') as outputfile:
        writer = csv.writer(outputfile)
        for item in ratio_list:
            write = [item]
            writer.writerow(write)
        np.savetxt(ratio_text, ratio_list, fmt ='%s')

print("success 6")
  
minimumChonk = min(ratio_list)
maximumChonk = max(ratio_list)
spectrum = 255 / (maximumChonk - minimumChonk)
for count in range(len(ratio_list)):
    ratio_list[count] *= spectrum
print("success 7")

#REBUILDING SECTION#
    
output_file = output_dir + "outputput.png"
grid = np.array(ratio_list)
grid2 = np.reshape(grid, (400,300))
colorImage = Image.fromarray(grid2)
colorImage = colorImage.convert("L")

colorImage = colorImage.rotate(-90)
#colorImage.save(output_file)

final_output = colorImage.resize((4000,3000))
final_output.save(output_file)
    
print("success 8")

    
    
    
    
    
    
    
    
    
    
    
    
