"""
small (0-500KB)
medium (500KB-1MB)
large (1MB-more)
"""
import os
import shutil

path_name = "random-files-master"


def which_bucket(size):
    if 0 < size < 500*1000:
        return "small"
    elif 500*1000 < size < 1000*1000:
        return "medium"
    else:
        return "large"

list_of_files = []
for dirpath, dirs, files in os.walk(path_name):
    for filename in files:
        fname = os.path.join(dirpath, filename)
        list_of_files.append(fname)

for file in list_of_files:
    if which_bucket(os.stat(file).st_size) == "small":
        if not os.path.exists("small"):
            os.makedirs("small")
        shutil.copy(file, "small")
    elif which_bucket(os.stat(file).st_size) == "medium":
        if not os.path.exists("medium"):
            os.makedirs("medium")
        shutil.copy(file, "medium")
    else:
        if not os.path.exists("large"):
            os.makedirs("large")
        shutil.copy(file, "large")
