import os
import sys
import subprocess
import json
import logging
import shutil
import yaml

from utils import get_video_files
from utils import get_unoptimized_video
from utils import get_video_dir
from utils import optimize_video

#TODO: recoger parametro de serie, pelicula o anime
#TODO: 1 Listar todos los contenidos del directorio actual
#TODO: Bucle para los contenidos, lee el metadata optimized
# y si no esta optimizado, lo optimiza

#for input_file in ./*.mkv; do ffmpeg -i "$input_file" -vcodec libx264 -b:v 2000k -preset medium -level:v 4.0 -pix_fmt yuv420p -profile:v high -c:a aac -b:a 159k -map 0  "./optimized/$(basename "${input_file%.*}").mkv"; done

logging.basicConfig(
  filename='logs/enhancer.log',
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

with open('config.yml', 'r') as file:
  directories = yaml.safe_load(file)

for source, settings in directories.items():
  source_contents = os.listdir(settings['path'])
  settings['contents'] = get_video_files(source_contents, settings['path'])
  settings['unoptimized_videos'] = []

  for video in settings['contents']:
    unoptimized_video = get_unoptimized_video(video)
    if(unoptimized_video):
      settings['unoptimized_videos'].append(unoptimized_video)

  print(settings['unoptimized_videos'])
  
  for video in settings['unoptimized_videos']:
    video_dir = get_video_dir(video)
    video_path = video.split('/')
    video_name = video_path[-1]

    new_video_path = f'{video_dir}/temp/{video_name}'

    optimize_video(video, new_video_path, video_dir, settings)

''' args = sys.argv[1:]

logging.basicConfig(
  filename='logs/enhancer.log',
  level=logging.INFO,
  format='%(asctime)s - %(levelname)s - %(message)s'
)

path = ''

if '-p' in args and args.index('-p') + 1:
  path = args[args.index('-p') + 1]

content_list = os.listdir(path)

def get_video_files(content_list, parent):
  files = []
  folders = []

  for content in content_list:
    if content.split('.')[-1] == 'mkv' or content.split('.')[-1] == 'mp4':
      files.append(parent + content);
    elif os.path.isdir(parent + content + '/'):
      folders.append(parent + content + '/')
  
  if(len(folders) > 0):
    for folder in folders:
      folder_contents = os.listdir(folder)
      files = files + get_video_files(folder_contents, folder)
  
  return files

video_files = get_video_files(content_list, path)
print(str(len(video_files)) + ' videos encontrados')

unoptimized_videos = []

for video in video_files:
  result = subprocess.run([
      'ffprobe',
      '-v', 'error',
      '-show_format',
      '-of', 'json',
      video
    ], stdout=subprocess.PIPE, stderr=subprocess.PIPE
  )

  video_data = json.loads(result.stdout)

  video_path = video.split('/')
  
  video_dir = video.split('/')
  video_dir.pop()
  video_dir = '/'.join(video_dir)

  video_name = video_path[-1]
  new_video_path = f'{video_dir}/temp/{video_name}'


  if not 'format' in video_data or not 'tags' in video_data['format'] or not 'OPTIMIZED' in video_data['format']['tags']:

    if not os.path.exists(f'{video_dir}/temp'):
      os.mkdir(f'{video_dir}/temp')

    command = f'ffmpeg -i "{video}" -metadata optimized=false -c copy "{new_video_path}"'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if(result.stderr):
      logging.error(f'There has been an error in {video}: \n {result.stderr}')
    if(result.stdout):
      logging.info(f'The optimized metadata has been added to the video {video} and set to false')

    if os.path.exists(new_video_path):
      shutil.move(new_video_path, video)
      unoptimized_videos.append(video)
  
  elif video_data['format']['tags']['OPTIMIZED'] == 'false':
    unoptimized_videos.append(video)

print(str(len(unoptimized_videos)) + ' videos sin optimizar') '''