import os
import logging
import yaml
import shutil
from utils import get_video_files, get_unoptimized_video, get_video_dir, optimize_video, check_video_size

GIGABITE_SIZE = 1024 ** 3

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
  
  for video in settings['unoptimized_videos']:
    video_dir = get_video_dir(video)

    video_path = video.split('/')
    video_name = video_path[-1]
    new_video_path = f'{video_dir}/temp/{video_name}'

    optimize_video(video, new_video_path, video_dir, settings, logging
)
    video_size = check_video_size(new_video_path)

    if os.path.exists(new_video_path) and video_size > 0:
      shutil.move(new_video_path, video)
      logging.info(f'''Video {new_video_path} moved succesfully to its original path {new_video_path}.\n
                   Video size: {video_size / GIGABITE_SIZE}GB''')
    else:
      logging.error(f'Video {video} has not been optimized because of an error. The original video has been restored.')