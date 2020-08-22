


import shutil
import os

source = '/Users/haydenstark/Downloads/Folder_a/'
destination = '/Users/haydenstark/Downloads/Folder_b/'
files = os.listdir(source)

for i in files:
    shutil.move(source+i, destination)
