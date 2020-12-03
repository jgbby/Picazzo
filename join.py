import cv2
import numpy as np

# Save Image
sliceFilePaths = [
    "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\sections\\sections-0.jpg",
    "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\sections\\sections-1.jpg",
    "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\sections\\sections-2.jpg
    
]
destPath = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\test.jpg"

final_image = []
for filepath in sliceFilePaths:
    sliceIMG = cv2.imread(filepath)
    for row in sliceIMG:
        final_image.append(row)

cv2.imwrite(destPath, np.asarray(final_image))