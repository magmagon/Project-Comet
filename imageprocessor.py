import os
import cv2

#image = cv2.imread()

ingest_dir = 'C:/Users/Magmagon/Pictures/Project-Comet-main/Edge Ranker/ingest/'
output_dir = 'C:/Users/Magmagon/Pictures/Project-Comet-main/Edge Ranker/temporary/'
readFileNameList = os.listdir(ingest_dir)
print(readFileNameList)

count = 0

width_dimension = 4000
height_dimension = 3000
resize_dimension = (width_dimension, height_dimension)
'''
for eachFile in readFileNameList:
    img = cv2.imread(eachFile)
    resized_image = cv2.resize(img, resize_dimension, interpolation = cv2.INTER_LINEAR)
    cv2.imwrite(output_dir + str(eachFile), resized_image)
    edges = cv2.Canny(resized_image, 100,200)
    cv2.imwrite(output_dir + str(eachFile) + "edge.jpg", edges)
'''

minval = [150,200,300]
maxval = [300,400,400]
img = cv2.imread(readFileNameList[0])
for x in range(len(minval)):
    edges = cv2.Canny(img, minval[x], maxval[x])
    cv2.imwrite(output_dir + str(x) + "edge.jpg", edges)
    print(minval[x], maxval[x])