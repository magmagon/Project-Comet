#This is the first alpha version of 'Edginess Detector'


#Importing the picture to be processed
import os
from skimage.io import io

#Processing image
import numpy as np
import skimage.io
from skimage import feature

#Write data to file
import csv

def Alpha():
    Alpha_ReadFileName = os.listdir('C:/Users/seagu/Pictures/Edge Ranker/ingest/')
    Alpha_FileName = Alpha_ReadFileName[0]
    Alpha_ImportFile = skimage.io.imread(fname= "C:/Users/seagu/Pictures/Edge Ranker/ingest/{}".format(Alpha_FileName))
    print("C:/Users/seagu/Pictures/Edge Ranker/ingest/{}".format(Alpha_FileName))
    #Alpha_ImportFile = PIL.Image.open('C:/Users/seagu/Pictures/Edge Ranker/ingest/input.jpg')
    #Alpha_ImageSize = Alpha_FileName.resize((1000,1000))
    Alpha_Gray = skimage.color.rgb2gray(Alpha_ImportFile)
    Alpha_Edges = feature.canny(Alpha_Gray, sigma = 1.5)
    skimage.io.imsave('C:/Users/seagu/Pictures/Edge Ranker/temporary/edges.jpg', arr=Alpha_Edges)

def Bravo():
    Bravo_ImportFile = skimage.io.imread(fname= "C:/Users/seagu/Pictures/Edge Ranker/temporary/edges.jpg")
    white_pixels = int(np.sum(Bravo_ImportFile == 255))
    black_pixels = int(np.sum(Bravo_ImportFile == 0))
    edge_ratio = (1000 * white_pixels / black_pixels)
    print("{:.8f}".format(edge_ratio))
    
    #Write to csv file
    write = ['Seed', edge_ratio]
    output = "C:/Users/seagu/Pictures/Edge Ranker/output/output.csv"

    with open(output, 'a', newline='') as outputfile:
        writer = csv.writer(outputfile)
        writer.writerow(write)

Alpha()
Bravo()