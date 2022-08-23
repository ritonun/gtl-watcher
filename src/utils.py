import os
import time


def get_creation_time_of_img(path, rename=False):
    mt = os.path.getmtime(path)
    ct = os.path.getctime(path)

    formating = '%Y:%m:%d %H:%M:%S'
    if rename:
        formating = '%Y%m%d_%H%H%S'

    ctime = time.strftime(formating, time.localtime(ct))
    mtime = time.strftime(formating, time.localtime(mt))
    
    oldest_time = mtime
    if ctime < mtime:
        oldest_time = ctime

    return oldest_time


def get_folder():
    folder_path = "../data/gtl_screen/"
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    full_files = []
    for f in files:
        full_files.append(folder_path + f)
    return full_files


def rename_folder():
    get_folder()

    list_name_used = []

    for file in files:
        path = folder_path + file
        old_name = get_creation_time_of_img(path, rename=True)
        name = str(old_name)

        index = 0
        while name in list_name_used:
            name = old_name + "_" + str(index)
            index += 1

        list_name_used.append(name)

        new_path = folder_path + name + '.png'
        os.rename(path, new_path)
