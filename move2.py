import cv2
import shutil
import os

import watchdog as wd

from_dir = (r'C:/Users/livcr/OneDrive/Pictures/bju/nbghost.jfif')
to_dir = (r'c:/Users/livcr/OneDrive/Pictures/projects')

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg'],
    "annoying_files":['.zip']
}

fileList = os.listdir(from_dir)


name, extension = os.path.splitext()


for key, value in dir_tree.items():
            
                 

                  if extension in value:

                    filename = os.path.basename()

                    path1 = from_dir + '/' + filename
                    path2 = from_dir + '/' + key
                    path3 = from_dir + '/' + key + '/' + filename

                    if os.path.exists(path2):
                      shutil.copy(path1,path3)
                      print('file moved')
                    else:
                      os.makedirs(path2)
                      shutil.copy(path1,path3)
                      print('directory created')