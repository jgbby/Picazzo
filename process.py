from PIL import Image, ImageOps
import numpy as np
import os


def RGB2Str(RGB):
    RGBStr = ''
    for value in RGB:
        RGBStr = RGBStr + str(round(value, 0)) + "-"
    return RGBStr

def getAverageRGB(img):

    pixels = img.shape[0] * img.shape[1]
    red = 0
    green = 0
    blue = 0
    for row in img:
        for pixel in row:
            red += pixel[0]
            green += pixel[1]
            blue += pixel[2]
    red /= pixels
    green /= pixels
    blue /= pixels
    dominant = [red, green, blue]  
    return dominant

def crop(img, dim):
    new_img = [] 
    for row in img[:dim]:
        new_img.append(row[:dim])
    return np.asarray(new_img)


def main():
    count = 0
    path = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\elli_paintings" 
    dest_path = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\elli_processed_paintings"
    for filename in os.listdir(path):

        # Get paths
        filepath = os.path.join(path, filename)
        dest_filepath = os.path.join(dest_path, "proc" + str(count) + ".jpg")
        print("Opening " + filepath + ", Saving in " + dest_filepath)

        # Open File and Crop
        img = Image.open(filepath)
        new_img = ImageOps.fit(img, (50, 50), method=Image.NEAREST, bleed=0.5)

        # Save files and overwrite
        if os.path.isfile(dest_filepath):
            os.remove(filepath)
            os.remove(dest_filepath)
        new_img.save(dest_filepath)
        count += 1
            


if __name__ == '__main__':
    main()