# 
# Python Problem Solver
# Week 13 Problem 2: The Messy Expedition Folder
#
import os
import shutil

def organise_by_type(folder):
    for name in os.listdir(folder):
        path = os.path.join(folder, name)
        if not os.path.isfile(path):
            continue  # skip subfolders, only move files

        _, ext = os.path.splitext(name)
        if ext and ext != '.':
            subfolder = ext[1:].lower()      # ".JPG" -> "jpg"
        else:
            subfolder = 'no_extension'        # README, .gitignore, etc.

        dest_dir = os.path.join(folder, subfolder)
        if not os.path.exists(dest_dir):
            os.mkdir(dest_dir)

        os.replace(path, os.path.join(dest_dir, name))
