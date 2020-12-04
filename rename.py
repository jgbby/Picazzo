import os

i = 0
path = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\processed_paintings"
for file in os.listdir(path):
    filepath = os.path.join(path, file)
    new_filepath = os.path.join(path, str(i) + "o" + ".jpg")
    os.rename(filepath, new_filepath)
    i += 1