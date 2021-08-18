# importing os and shutil
import os
import shutil

# Taking location of the folder whose files have to be backuped
source = input("Enter the source folder name: ")

# Taking location of the folder where files have to be backuped
destination = input("Enter the destination folder name: ")

source = source + '/'
destination = destination + '/'

# Storing all the files present in that folder in fileList variable
listOfFiles = os.listdir(source)

# Moving files from one folder to another
# for file in listOfFiles:
#    shutil.move((source+file), destination)

# Coping files from one folder to another
for file in listOfFiles:
    shutil.copy((source+file), destination)
