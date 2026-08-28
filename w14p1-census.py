# 
# Python Problem Solver
# Week 14 Problem 1: The Field Guide Census
#

import os

def census(root):
    file_count = 0
    total_size = 0
    biggest_path = None
    biggest_size = -1

    for dirpath, dirnames, filenames in os.walk(root):
        for name in filenames:
            path = os.path.join(dirpath, name)
            size = os.path.getsize(path)

            file_count += 1
            total_size += size

            if size > biggest_size:
                biggest_size = size
                biggest_path = path

    print(f"Files found : {file_count}")
    print(f"Total size  : {total_size} bytes")
    if biggest_path is not None:
        print(f"Biggest file: {biggest_path} ({biggest_size} bytes)")
    else:
        print("Biggest file: (none)")

census(".")
