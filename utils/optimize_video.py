# utils/optimize_video.py

import os
import subprocess

def optimize_video(current_path, new_path, current_dir, settings, logging):

  command = "ffmpeg "
  command += f"-i '{current_path}' "
  command += "-metadata optimized=1 "
  command += f"-vcodec {settings.get('codec', 'libx265')} "
  command += f"-crf {settings.get('crf', 18)} "
  command += f"-preset {settings.get('preset', 'slow')} "
  command += f"-level:v {settings.get('level', '5.1')} "
  command += f"-pix_fmt {settings.get('pixels', 'yuv420p')} "
  command += f"-profile:v {settings.get('profile', 'main')} "
  command += f"-c:a {settings.get('audio', 'ac3')} "
  command += f"-b:a {settings.get('arate', '192k')} "
  command += "-c:s copy "
  command += "-map 0 "
  command += f"'{new_path}'"
  
  if not os.path.exists(f'{current_dir}/temp'):
    os.mkdir(f'{current_dir}/temp')
    
  logging.info(f'Optimizing {current_path}.')
  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
  if result.stdout:
    logging.info(f'Video {current_path} optimized succesfully')
    
  if result.stderr:
    logging.warning(f'There has been an error in {current_path} while using: \n{command}')