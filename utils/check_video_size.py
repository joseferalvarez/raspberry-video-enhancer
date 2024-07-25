# utils/check_video.py

import subprocess
import json
import os

def check_video_size(video):
    result = subprocess.run([
      'ffprobe',
      '-v', 'error',
      '-show_format',
      '-of', 'json',
      video
      ], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    ) 
    video_data = json.loads(result.stdout)

    if not 'format' in video_data or not 'tags' in video_data['format'] or not 'OPTIMIZED' in video_data['format']['tags'] or video_data['format']['tags']['OPTIMIZED'] == "0":
      return 0
    
    if os.path.getsize(video) > 0 and video_data['format']['tags']['OPTIMIZED'] == 1:
      return os.path.getsize(video)
    
    return 0