import glob
import os
import subprocess

# conda install -c anaconda ffmpeg
# make sure the audio/test audio/dev audio/train folders exist

OUTPUT_PATH = os.path.join('data', 'audio')

files = glob.glob(os.path.join('data', 'video', '*', '*.mp4'))

for file in files:
    output_file = file.replace('video', 'audio').replace('.mp4', '.wav')
    print("Extracting audio from %s to %s" % (file, output_file))
    command = "ffmpeg -i %s -y -ab 160k -ac 2 -ar 44100 -vn %s 2> /dev/null" % (file, output_file)
    subprocess.call(command, shell=True)
