# utils/get_video_dir.py

def get_video_dir(video):
  video_dir = video.split('/')
  video_dir.pop()
  video_dir = '/'.join(video_dir)

  return video_dir