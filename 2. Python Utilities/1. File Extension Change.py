# Date: 21/9/2017
# Name: file_extn_change.py
#
'''
Change the extention of a group of spficific files in a folder
'''

__version__ = '1.0'

import os
import sys


def file_rename(work_dir, old_ext, new_ext):
    """ renames the files with specific extentions to
    new extentions """
    File_count = 0
    File_rnm_count = 0

    for filename in os.listdir(work_dir):
        File_count += 1
        # Get the file extention
        file_ext = os.path.splitext(filename)[1]

        # Check if the file has the extention you wanted to chagne
        if old_ext == file_ext:
            File_rnm_count += 1
            # change the extention of the file
            newname = filename.replace(old_ext, new_ext)
            # Rename the files in the folder
            os.rename(os.path.join(work_dir, filename),
                      os.path.join(work_dir, newname)
                      )
    print("Number of files in folder : ", File_count)
    print("Number of files renamed   : ", File_rnm_count)

# below line is for interactive run in IDLE
# file_rename(r"C:\Users\sam\Desktop\DS\Python\Test", ".pdf", ".txt")


def main():
    '''This main function will be called if the script is directly invoked
    '''
    # first argument from batch
    work_dir = sys.argv[1]
    # 2nd arg from batch
    old_ext = sys.argv[2]
    # 3rd arg from batch
    new_ext = sys.argv[3]

    # call the rename function with the passed arguments
    file_rename(work_dir, old_ext, new_ext)


if __name__ == '__main__':
    main()
