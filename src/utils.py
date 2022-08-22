import os
import time

def get_creation_time_of_img(path):
    mt = os.path.getmtime(path)
    ct = os.path.getctime(path)

    ctime = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(ct))
    mtime = time.strftime('%Y:%m:%d %H:%M:%S', time.localtime(mt))
    
    oldest_time = mtime
    if ctime < mtime:
        oldest_time = ctime

    return oldest_time
