import numpy as np
import cv2
import csv
import os

#this program splits the image into 100 separate rectangles, analyze edge ratio and send to csv
x_pixel = 0
y_pixel = 0

#import image
input_dir = "C:/Users/seagu/Pictures/ProjectComet/temporary/"
output_dir = "C:/Users/seagu/Pictures/ProjectComet/temporary/chunks/"

FileNameList = os.listdir(input_dir)
output = "C:/Users/seagu/Pictures/ProjectComet/output/split.csv"

for eachFile in FileNameList:
    print(eachFile)
    image = cv2.imread(eachFile)
    dimensions = image.shape
    print(dimensions)

    x_split = int(dimensions[1] / 10)
    y_split = int(dimensions[0] / 10)
    print("split",x_split, y_split)

    ratio_list = []

    for x_iteration in range(10):
        for y_iteration in range(10):
            split_image = image[x_pixel:x_pixel + x_split,y_pixel:y_pixel+y_split]
            white_pixels = int(np.sum(split_image == 255))
            black_pixels = int(np.sum(split_image == 0))
            ratio = (1000 * white_pixels / (black_pixels + 1))
            ratio_list.append(ratio)
            print("x,y", x_pixel, y_pixel)
  
            #print("iteration", x_iteration, y_iteration)
            #cv2.imwrite(output_dir + str(x_iteration + y_iteration) + ".jpg", split_image)
            y_pixel += y_split

        x_pixel += x_split
        y_pixel = 0
    break

with open(output, 'w', newline = '') as outputfile:
    writer = csv.writer(outputfile)
    for item in ratio_list:
        write = [item]
        writer.writerow(write)
        print(item)

minimumChonk = min(ratio_list)
maximumChonk = max(ratio_list)

print(ratio_list)
print(minimumChonk, maximumChonk)

