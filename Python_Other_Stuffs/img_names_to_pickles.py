import os
import pickle
"""
path = "../RESULTS_selected/"

total = 0

img_paths = {}
for day in os.scandir(path):
    img_paths[day.name] = {}
    for cam in os.scandir(day.path):
        if "new_deleted" in cam.name:
            continue
        img_paths[day.name][cam.name] = [i.path for i in os.scandir(cam.path) if ".jpg" in i.name]

        total += len(img_paths[day.name][cam.name])

print(total)
with open(r"./img_paths.pickle", "wb") as output_file:
    pickle.dump(img_paths, output_file)
"""

# read it
import pandas as pd

file_name = "./img_paths.pickle"
objects = pd.read_pickle(file_name)
print(objects)

