# utils/get_video_files.py

import os

def get_video_files(contents, parent):
  files = []
  folders = []

  for content in contents:
    if content.split('.')[-1] == 'mkv' or content.split('.')[-1] == 'mp4':
      files.append(parent + content);
    elif os.path.isdir(parent + content + '/'):
      folders.append(parent + content + '/')
  
  if(len(folders) > 0):
    for folder in folders:
      folder_contents = os.listdir(folder)
      files = files + get_video_files(folder_contents, folder)
  
  return files