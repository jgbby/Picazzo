import cv2
import numpy as np

# Save Image
sliceFilePath = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\sections\\sections-"
destPath = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\test4.jpg"

final_image = []
for i in range(6):
    fileEnd = str(i) + ".jpg"
    filepath = sliceFilePath + fileEnd
    sliceIMG = cv2.imread(filepath)
    for row in sliceIMG:
        final_image.append(row)

cv2.imwrite(destPath, np.asarray(final_image))