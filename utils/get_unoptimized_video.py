# utils/get_unoptimized_video.py

import subprocess
import json

def get_unoptimized_video(video):
    
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
      return video
  
    return