import os
path = '../Functions'
# os.listdir(path)
all_files = os.listdir(path)

for files in all_files :
    if os.path.isfile(os.path.join(path, files)):
        print("{} is a file".format(files))