#This is the first alpha version of 'Edginess Detector'


#Importing the picture to be processed
import os

#Processing image
import numpy as np
import skimage.io
from skimage import feature
from skimage.feature import blob_dog, blob_log, blob_doh

import csv

def Alpha():
    #name directory
    Alpha_ReadFileName = os.listdir('C:/Users/seagu/Pictures/Edge Ranker/ingest/')
    Alpha_FileName = Alpha_ReadFileName[0]
    #ingest picture
    Alpha_ImportFile = skimage.io.imread(fname= "C:/Users/seagu/Pictures/Edge Ranker/ingest/{}".format(Alpha_FileName))
    print("C:/Users/seagu/Pictures/Edge Ranker/ingest/{}".format(Alpha_FileName))
    #Alpha_ImportFile = PIL.Image.open('C:/Users/seagu/Pictures/Edge Ranker/ingest/input.jpg')
    #Alpha_ImageSize = Alpha_FileName.resize((1000,1000))
    Alpha_Gray = skimage.color.rgb2gray(Alpha_ImportFile)
    Alpha_log = blob_log(Alpha_Gray, max_sigma=30, num_sigma=10, threshold=.1)
    Alpha_dog = blob_dog(Alpha_Gray, max_sigma=30, threshold=.1)
    Alpha_doh = blob_doh(Alpha_Gray, max_sigma=30, threshold=0.1)
    skimage.io.imsave('C:/Users/seagu/Pictures/Edge Ranker/temporary/blob_log', arr=Alpha_log)
#    skimage.io.imsave('C:/Users/seagu/Pictures/Edge Ranker/temporary/blob_dog.jpg', arr=Alpha_dog)
#    skimage.io.imsave('C:/Users/seagu/Pictures/Edge Ranker/temporary/blob_doh.jpg', arr=Alpha_doh)

def Bravo():
    Bravo_ImportFile = skimage.io.imread(fname= 'C:/Users/seagu/Pictures/Edge Ranker/temporary/blob.jpg')
    Bravo_Gray = skimage.color.rgb2gray(Bravo_ImportFile)
    white_pixels = int(np.sum(Bravo_ImportFile == 255))
    black_pixels = int(np.sum(Bravo_ImportFile == 0))
    edge_ratio = (white_pixels / black_pixels)
    print(edge_ratio)

    #Write to csv file
    write = ['Seed', edge_ratio]
    output = "C:/Users/seagu/Pictures/Edge Ranker/output/blobtest.csv"

    with open(output, 'a', newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(write)

Alpha()
Bravo()