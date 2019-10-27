import shutil
import os
from constants import CSV, DESTINATION_BASE_URL,DESTINATION_PNG_URL, SOURCE_BASE_URL, IMAGE_TYPE, DESTINATION_CSV_URL, DESTINATION_THUMBNAIL_URL, VIDEO_TYPE, DESTINATION_IMAGE_URL, DESTINATION_TEMP
from image_process import get_file_size, get_base_filename, get_file_extension, copy_file
from progress.bar import Bar
import time 
import logging

logging.basicConfig(filename='logname',
                            filemode='a',
                            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                            datefmt='%H:%M:%S',
                            level=logging.DEBUG)

# logging.info("Running Urban Planning")
logger = logging.getLogger('urbanGUI')
if not os.path.exists(DESTINATION_BASE_URL):
    os.makedirs(DESTINATION_BASE_URL)
if not os.path.exists(DESTINATION_THUMBNAIL_URL):
    os.makedirs(DESTINATION_THUMBNAIL_URL)
if not os.path.exists(DESTINATION_IMAGE_URL):
    os.makedirs(DESTINATION_IMAGE_URL)
if not os.path.exists(DESTINATION_TEMP):
    os.makedirs(DESTINATION_TEMP)
if not os.path.exists(DESTINATION_CSV_URL):
    os.makedirs(DESTINATION_CSV_URL) 
if not os.path.exists(DESTINATION_PNG_URL):
    os.makedirs(DESTINATION_PNG_URL) 
    
for folderName, subfolders, filenames in os.walk(SOURCE_BASE_URL):
    print('Scanning folder: ',folderName)
    print(len(subfolders), ' subfolders')
    files = [filename for filename in filenames if not filename[0] == '.']
    total_files = len(files)
    bar = Bar('Processing', max=total_files)

    for filename in files:
        bar.next()
        if folderName == SOURCE_BASE_URL:
            filename = folderName + filename
        else:
            filename = folderName + '/' + filename
        file_extension = get_file_extension(filename)
        if file_extension in IMAGE_TYPE:
            if get_file_size(filename) > 50920:
                copy_file(filename, DESTINATION_IMAGE_URL)
            else:
                copy_file(filename, DESTINATION_THUMBNAIL_URL)
        elif file_extension == '.png':
            if get_file_size(filename) > 50920:
                copy_file(filename, DESTINATION_PNG_URL)
            else:
                logging.info(filename)
        elif file_extension in CSV:
            copy_file(filename, DESTINATION_CSV_URL)
        else:
            logging.info(filename)
        # else:
        #     copy_file(filename, DESTINATION_TEMP)
    bar.finish()

print('Completed!')



