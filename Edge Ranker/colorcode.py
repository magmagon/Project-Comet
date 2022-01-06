import numpy as np
import csv


with open("C:/Users/seagu/Pictures/Edge Ranker/output/split.csv", 'r') as inputFile:
    reader = csv.reader(inputFile, delimiter=',')
    ratios = []

    for item in reader:
        ratios.append(float(item[0]))

#print(ratios)
minimumChonk = min(ratios)
maximumChonk = max(ratios)
#print(minimumChonk, maximumChonk)

#spectrum section
spectrum = 255 / (maximumChonk - minimumChonk)

print(spectrum)
for count in range(len(ratios)):
    ratios[count] *= spectrum

print(ratios)

grid = np.asarray(ratios)
grid2 = np.reshape(grid, (10,10))
print(grid2)