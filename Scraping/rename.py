import os
os.getcwd()
collection = "Dataset/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("Dataset/" + filename, "Dataset/" + str(i) + ".png")