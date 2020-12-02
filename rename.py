import os

i = 0
path = os.path.join(os.getcwd(), "renamed")
path = "C:\\Users\\xlqgi\\DEV\\Friends\\Picazzo\\elli_folder"
for file in os.listdir(path):
    filepath = os.path.join(path, file)
    new_filepath = os.path.join(path, str(i) + ".jpg")
    os.rename(filepath, new_filepath)
    i += 1