SOURCE_BASE_URL = '/Volumes/TOSHIBA EXT/'
DESTINATION_BASE_URL = '/Volumes/naaju/backup1'
DESTINATION_DIR_OTHERS = DESTINATION_BASE_URL + 'Others'

DESTINATION_IMAGE_URL = DESTINATION_BASE_URL + '/images/'
DESTINATION_THUMBNAIL_URL = DESTINATION_BASE_URL + '/thumbnail/'
DESTINATION_TEMP = DESTINATION_BASE_URL + '/temp/'
DESTINATION_CSV_URL = DESTINATION_BASE_URL + '/csv/'
DESTINATION_PNG_URL = DESTINATION_BASE_URL + '/png/'

DESTINATION_DIR = {
    # Text
    '.txt': DESTINATION_BASE_URL + "Doc",
    '.pdf': DESTINATION_BASE_URL + "Doc",
    '.mkv': DESTINATION_BASE_URL + "Video",
    '.mp4': DESTINATION_BASE_URL + "Video",
    # Images
    '.jpg': DESTINATION_BASE_URL + "Images",
    '.jpeg': DESTINATION_BASE_URL + "Images",
    '.png': DESTINATION_BASE_URL + "Images",
    '.ps': DESTINATION_BASE_URL + "Images",
}

IMAGE_TYPE = ['.jpg', '.jpeg','.ps', '.mov','HEIF','HEIC','heif','heic']
VIDEO_TYPE = ['.WEBM','.mkv', '.mp4', '.m4p', '.m4v', 'svg','.avi','plist','txt','.xml','.class','.html','.h']
CSV = ['.csv']
