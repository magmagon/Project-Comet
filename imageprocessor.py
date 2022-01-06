import os
import cv2

#image = cv2.imread()
#ingest_dir = 'C:/Users/Magmagon/Pictures/Project-Comet-main/ProjectComet/ingest/'
#output_dir = 'C:/Users/seagu/Pictures/ProjectComet/temporary/'
#readFileNameList = os.listdir(input_dir)
#print(readFileNameList)


input_dir = 'C:/Users/seagu/Pictures/ProjectComet/ingest'
output_dir = 'C:/Users/seagu/Pictures/ProjectComet/temporary/'
FileNameList = os.listdir(input_dir)
print(FileNameList)

count = 0

width_dimension = 4000
height_dimension = 3000
resize_dimension = (width_dimension, height_dimension)

#img = cv2.imread("C:/Users/seagu/Pictures/ProjectComet/ingest/112082unimgNoise70.jpg")
#cv2.imshow("image",img)
#cv2.waitKey()


for eachFile in FileNameList:
    print(eachFile)
    img = cv2.imread(eachFile)
#    cv2.imshow("before", img)
    
#    cv2.imwrite(output_dir + str(eachFile) + "resized.jpg", resized_image)
    edges = cv2.Canny(img, 100,200)
    resized_image = cv2.resize(edges, resize_dimension, interpolation = cv2.INTER_LINEAR)
#    cv2.imshow("image", resized_image)
#    cv2.imshow("edge", edges)
#    cv2.waitKey()
    output_dir += str(eachFile)
    print(output_dir)
    cv2.imwrite(output_dir + str(eachFile) + "edge.jpg", resized_image)


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