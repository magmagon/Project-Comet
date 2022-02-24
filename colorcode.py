import numpy as np
import csv
from PIL import Image

with open("C:/Users/seagu/Pictures/ProjectComet/output/split.csv", 'r') as inputFile:
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

print(type(ratios))

grid = np.array(ratios)
grid2 = np.reshape(grid, (40,30))
print(grid2)

print(type(grid2))
colorImage = Image.fromarray(grid2)
colorImage = colorImage.convert("L")
colorImage.save("C:/Users/seagu/Pictures/ProjectComet/output/color.png")
output = colorImage.resize((4000,3000))
output.save('C:/Users/seagu/Pictures/ProjectComet/output/upscaled.png')