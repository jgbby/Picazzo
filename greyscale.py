import cv2

img = cv2.imread("C:\\Users\\xlqgi\dev\\friends\\picazzo\\src\\rama_ravana.jpg", cv2.IMREAD_GRAYSCALE)

try:
    cv2.imwrite("C:\\Users\\xlqgi\\dev\\friends\\picazzo\\src\\rama_ravana_grey.jpg", img)
except FileNotFoundError:
    print("Can't find rama_ravana.jpg")
