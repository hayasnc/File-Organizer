from PIL import Image
import os
from constants import DESTINATION_DIR, SOURCE_BASE_URL, DESTINATION_DIR_OTHERS, DESTINATION_BASE_URL
import shutil

# filename = '/Users/hayasnc/Desktop/photo.jpg'
# im = Image.open(filename)
# statinfo = os.stat(filename)
# print(statinfo)
# # print(im.info)
# width, height = im.size

def copy_file(source, destination_dir_path):
    destination = destination_dir_path + get_base_filename(source)
    # print(destination)
    return shutil.copyfile(source, destination) 


def get_file_size(filepath):
    statinfo = os.stat(filepath)
    return statinfo.st_size

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

def get_base_filename(filename):
    return os.path.basename(filename)

def get_filename_without_extension(filename):
    return os.path.splitext(filename)[0]

def get_file_extension(filename):
    return os.path.splitext(filename)[1]

def create_thumbnail(filename, X=128, Y=128):
    MAX_SIZE = (X, Y)
    im = Image.open(filename)
    im.thumbnail(MAX_SIZE)
    im.save(DESTINATION_BASE_URL + get_base_filename(filename))


def resize(imageFile):
    im1 = Image.open(imageFile)
    # adjust width and height to your needs
    width = 500
    height = 420
    # use one of these filter options to resize the image
    im2 = im1.resize((width, height), Image.NEAREST)      # use nearest neighbour
    im3 = im1.resize((width, height), Image.BILINEAR)     # linear interpolation in a 2x2 environment
    im4 = im1.resize((width, height), Image.BICUBIC)      # cubic spline interpolation in a 4x4 environment
    im5 = im1.resize((width, height), Image.ANTIALIAS)    # best down-sizing filter
    ext = ".jpg"
    im2.save("NEAREST" + ext)
    im3.save("BILINEAR" + ext)
    im4.save("BICUBIC" + ext)
    im5.save("ANTIALIAS" + ext)

# for folderName, subfolders, filenames in os.walk(SOURCE_BASE_URL):
    # print('Started!!')
    # files = [filename for filename in filenames if not filename[0] == '.']
    # for filename in files:
    #     if folderName == SOURCE_BASE_URL:
    #         filename = folderName + filename
    #     else:
    #         filename = folderName + '/' + filename
    #     process_file(filename)
# resize(filename)
# print('Complete!!')



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