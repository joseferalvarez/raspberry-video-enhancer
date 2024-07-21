# utils/optimize_video.py

import os
import subprocess
import shutil

def optimize_video(current_path, new_path, current_dir, settings):
  command = "ffmpeg "
  command += f"-i {current_path} "
  command += "-metadata optimized=1 "
  command += f"-vcodec {settings['codec']} " if settings['codec'] else "-vcodec libx264 "
  command += f"-b:v {settings['bitrate']} " if settings['bitrate'] else "-b:v 4000k "
  command += f"-preset {settings['preset']} " if settings['preset'] else "-preset medium "
  command += f"-level:v {settings['level']} " if settings['level'] else "-level:v 4.0 "
  command += f"-pix_fmt {settings['pixels']} " if settings['pixels'] else "-pix_fmt yuv420p "
  command += f"-profile:v {settings['profile']} " if settings['profile'] else "-profile:v high "
  command += f"-c:a {settings['audio']} " if settings['audio'] else "-c:a aac "
  command += f"-b:a {settings['arate']} " if settings['arate'] else "-b:a 159k "
  command += "-map 0 "
  command += new_path

  if not os.path.exists(f'{current_dir}/temp'):
    os.mkdir(f'{current_dir}/temp')

  result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

  if os.path.exists(new_path):
    shutil.move(new_path, current_path)