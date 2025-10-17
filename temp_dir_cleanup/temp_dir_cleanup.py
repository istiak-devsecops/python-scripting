# Automated Temp Directory Cleanup

import os
import shutil
import datetime

temp_dir="/tmp" # temp file dir
days_old=7   # Files older than this will be deleted

now = datetime.datetime.now()   # store the value of current date and time
delete_file = now - datetime.timedelta(days=days_old) # stored the value time between the files needs to be deleted

deleted_files = 0   # store how many files deleted
deleted_dirs = 0    # store how many dir deleted

for root, dirs, files in os.walk(temp_dir, topdown=False): # delete old files
    for name in files:
        file_path = os.path.join(root, name)    # make the full path with the current or root dir 
        try:
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(file_path))    # get the file age
            if mtime < days_old:
                os.remove(file_path)    # delet empty old file
                deleted_files += 1
        except Exception as e:
            print(f"Error deleting file {file_path}: {e}")
    
    for name in dirs:
        dir_path = os.path.join(root, name)     # make a full dir path 
        try:
            mtime = datetime.datetime.fromtimestamp(os.path.getmtime(dir_path))     # get dir age
            if mtime < days_old and not os.listdir(dir_path):   # check the dir age is less than 7 and the dir is not empty
                shutil.rmtree(dir_path)     # remove dir and its content recursively
                deleted_dirs += 1
        except Exception as e:
            print(f"Error deleting directory {dir_path}: {e}")
        
print(f"cleanup complete. Deleted {deleted_files} files and {deleted_dirs} directories older than {days_old} days.")


