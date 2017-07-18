'''
This script finds all dupe files in a given folder.
File dupe is file with same size and same name.

Anton Demkin, 2017
antondemkin#yandex.ru

'''

import os
import sys


def get_file_list(folder):
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            path = os.path.join(dirpath, filename)
            size = os.path.getsize(path)
            folder_info = (dirpath, filename, size)
            files.append(folder_info)
    return files


def get_dupes(filelist):
    all_files = []
    dupes = []
    for path, filename, size in filelist:
        current = {(filename, size)}
        if current in all_files:
            dupes.append(os.path.join(path, filename))
        else:
            all_files.append(current)
    return dupes


def main():
    if len(sys.argv) > 1:
        path = sys.argv[1]
        if os.path.exists(path):
            all_files = get_file_list(path)
            dupes = get_dupes(all_files)
            if len(dupes) > 0:
                print("%d duplicate files found." % len(dupes))
        else:
            print('%s is not a valid path' % path)
    else:
        print("usage: python duplicates.py [folder]")


if __name__ == "__main__":
    main()
