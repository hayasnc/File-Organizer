import shutil
import os
from constants import DESTINATION_DIR, SOURCE_BASE_URL, DESTINATION_DIR_OTHERS

def process_file(filename):
    extension = 'noname'
    try:
        extension = str(os.path.splitext(SOURCE_BASE_URL + filename)[1])
    except Exception:
        extension = 'noname'
    try:
        directory_destination_path = DESTINATION_DIR[extension]
    except KeyError as message:
        print(message)
        directory_destination_path = DESTINATION_DIR_OTHERS
    if not os.path.exists(directory_destination_path):
        os.mkdir(directory_destination_path)
    print('Moving...', filename, ' to ' , directory_destination_path)
    try:
        shutil.move(filename , directory_destination_path)

    except shutil.Error as e:
        print('WARNING!!! ' + str(e))
        val = input("Do you want to overwrite?(y/n)")
        if val=='y':
            shutil.move(filename, os.path.join(directory_destination_path, os.path.basename(filename)))
            print('Overwrited')

for folderName, subfolders, filenames in os.walk(SOURCE_BASE_URL):
    print('Started!!')
    files = [filename for filename in filenames if not filename[0] == '.']
    for filename in files:
        if folderName == SOURCE_BASE_URL:
            filename = folderName + filename
        else:
            filename = folderName + '/' + filename
        process_file(filename)

print('Complete!!')
