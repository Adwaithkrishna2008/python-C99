import os
import shutil

source=input('Enter the Source here: ')
dest=input('Enter the dest here: ')
source=source+"/"
dest=dest+"/"
list_of_files=os.listdir(source)
for file in list_of_files:
    shutil.copy((source+file),dest)