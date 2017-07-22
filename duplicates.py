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

def print_dupes_info(dupes):
    if len(dupes) > 0:
        print("%d duplicate files found:" % len(dupes))
        for dupe in dupes:
            print(dupe)
    else:
        print('No duplicate files found.')


def main():
    path = sys.argv[1]
    if os.path.exists(path):
        all_files = get_file_list(path)
        dupes = get_dupes(all_files)
        print_dupes_info(dupes)
    else:
        print('%s is not a valid path' % path)


if __name__ == "__main__":
    main()
