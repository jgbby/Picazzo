import os
from PIL import Image
import numpy as np
from math import sqrt
import cv2
import copy

def getAverageRGB(image):
    im = np.array(image)
    if  len(im.shape) == 3:
        w, h, d = im.shape
        return (tuple(np.average(im.reshape(w * h, d), axis=0)))
    else:
        return [0, 0, 0]


def processImages(path):
    filenames = []
    meanRGBs = []

    for file in os.listdir(path):
        filepath = os.path.join(path, file)
        img = Image.open(filepath)

        filenames.append(file)
        meanRGBs.append(
            [int(val) for val in getAverageRGB(img)]
        )
    return filenames, meanRGBs


def distance2Color(rgb1, rgb2):
    sum = 0
    for i in range(len(rgb1)):
        sum += (pow(rgb1[i] - rgb2[i], 2))
    return sqrt(sum)


def getPaintingIndex(rgb, meanRGBs):
    curIndex = 0
    betaIndex = 0
    betaDistance = float('inf')

    for meanRGB in meanRGBs:
        colorDistance = distance2Color(meanRGB, rgb)
        if colorDistance < betaDistance:
            betaIndex = curIndex
            betaDistance = colorDistance 

        curIndex += 1
    return betaIndex


def main():


    # Likely an issue with channels being in wrong order, I get inverted color schemes


    # PARAMETERS
    dim = 50
    no_repeat = False
    
    #fileName = sys.argv[1]
    filename = 'ellinjamie.jpg'
    srcPath = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\src\\" + filename
    destPath = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\mosaic\\mosaic-" + filename
    thumbnailPath = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\thumbnails\\image-thumbnail-" + filename
    paintingSourcePath = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\processed_paintings"


    # Image Processing to reduce dimensions of srcFile
    img = Image.open(srcPath)
    img.thumbnail((400, 400))
    img.save(thumbnailPath)


    # Initialize create_image
    create_image = []   
    create_image_index = 0


    # Process resized images
    filenamesO, meanRGBsO = processImages(paintingSourcePath)
    filenames = copy.copy(filenamesO)
    meanRGBs = copy.copy(meanRGBsO)

    # Iterate image 
    img = cv2.cvtColor(cv2.imread(thumbnailPath), cv2.COLOR_BGR2RGB)
    for rowNum in range(len(img)):

        # Instantiate 50 empty rows for every row in our thumbnail
        for i in range(dim):
            create_image.append([])


        # Iterate pixels and retrieve corresponding painting
        row = img[rowNum]
        for pixelNum in range(len(row)):
            pixel = row[pixelNum]


            # Identify painting (remove copies)
            paintingIndex = getPaintingIndex(pixel, meanRGBs)
            paintingName = filenames[paintingIndex]
            path2Painting = os.path.join(paintingSourcePath, paintingName)
            painting = cv2.imread(path2Painting)

            if no_repeat:
                filenames.remove(paintingName)
                meanRGBs.pop(paintingIndex)

                # Check if we've gone through all paintings
                if len(filenames) == 1:
                    filenames = copy.copy(filenamesO)
                    meanRGBs = copy.copy(meanRGBsO)


            # Populate image with either painting or enlarged pixels
            for i in range(create_image_index,  create_image_index + dim):
                for j in range(dim):
                    create_image[i].append(painting[i - create_image_index][j])


            
            print("ROW: " + str(rowNum) + ", PIXEL: " + str(pixelNum))
        
        create_image_index += dim
        #cv2.imwrite('test.jpg', np.asarray(create_image))

    # Save Image
    cv2.imwrite(destPath, np.asarray(create_image))




if __name__ == "__main__":
    main()