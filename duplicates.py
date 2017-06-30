'''
This script finds all dupe files in a given folder.
File dupe is file with same size and same name.

Anton Demkin, 2017
antondemkin#yandex.ru

'''

import os
import sys


def get_file_list(folder):
    '''
    This function returns a list of tuples with
    'path', 'filename' and 'size' of all files in a given folder.
    '''
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for filename in filenames:
            # get file size
            path = os.path.join(dirpath, filename)
            size = os.path.getsize(path)
            # other way to get file size
            # info = os.stat(path)
            # size = info.st_size
            
            folder_info = [dirpath, filename, size]
            files.append(folder_info)
    return files


def get_dupes(filelist):
    '''
    This function read a list in a format:
    ['path','filename','size'] and returns new list with path+filename of duplicate files
    '''
    all_files = []
    dupes = []
    
    for path, filename, size in files:
        current = dict([(filename, size)])
        if current in all_files:
            dupes.append(os.path.join(path, filename))
        else:
            all_files.append(current)
    
    return dupes


def ask_to_delete(dupes):
    if len(dupes) > 0:
        answer = ''
        while answer != 'y' or 'n':
            answer = input('%d dupe files found. Remove them? y/n: ' % len(dupes))
            if answer == 'y':
                # remove all dupes
                print('remove all dupes:')
                for dupe in dupes:
                    print('removing %s' % dupe)
                    os.remove(dupe)
                break
            if answer == 'n':
                # dont remove dupes
                print('No dupes were harmed.')
                break
            else:
                print('y/n: ')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        path = sys.argv[1:]
        for i in path:
            if os.path.exists(i):
                # get all files in a given dir
                files = get_file_list(i)
                # find dupes from all files
                dupes = get_dupes(files)
                # if dupes found, ask what to do next
                ask_to_delete(dupes)
            else:
                print('%s is not a valid path' % i)
                sys.exit()
    else:
        print("usage: python duplicates.py [folder]")
        
