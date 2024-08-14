# Raspberry video enhancer

Optimize thousands of videos with one script with the same config.

## Instructions

### Installing the packages

```bash
git clone https://github.com/joseferalvarez/raspberry-video-enhancer.git

cd raspberry-video-enhancer.git

python3 -m venv ./env

source env/bin/activate

pip3 install -r requirements.txt
```

### Set the config

1. Copy the template.config.yml to config.yml.
2. You can set the system paths with the videos in config.yml, every path gets the videos recursively.
3. Set the config of each path. All the videos on this path will get that config.

Example with all the config params. At the back, uses ffmpeg to optimize the videos:

```yml
source:
  path: /your/source/path/
  codec: libx264
  bitrate: 6000k
  preset: medium
  level: "4.0"
  pixels: yuv420p
  profile: high
  audio: aac
  arate: 159k
```

### Exec the script

```bash
python3 video_enhancer.py
```
