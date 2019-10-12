import shutil
import os
from constants import DESTINATION_DIR, SOURCE_BASE_URL, DESTINATION_DIR_OTHERS

files = os.listdir(SOURCE_BASE_URL)
for filename in files:
    extension = 'noname'
    try:
        extension = str(os.path.splitext(SOURCE_BASE_URL + filename)[1])
    except Exception:
        extension = 'noname'
    try:
        directory_destination_path = DESTINATION_DIR[extension]
    except KeyError as message:
        print(message)
        folder_destination_path = DESTINATION_DIR_OTHERS
    if not os.path.exists(directory_destination_path):
        os.mkdir(directory_destination_path)

    shutil.move(SOURCE_BASE_URL + filename, directory_destination_path)
