from pytube import YouTube
import os
import urllib.request
import re
import shutil
import sys

location = ' '.join(sys.argv)
file = location.replace('f:/My Python Projects/Yt To Mp3/file_rep.py ', '')

def remove_line():
    with open(file, 'r') as fr:
        lines = fr.readlines()
        ptr = 0
        with open('songs.txt', 'w') as fw:
            for line in lines:
                if ptr != 0:
                    fw.write(line)
                ptr += 1

if os.path.exists('error_file.txt'):
    pass
else:
    try:
        open('error_file.txt', 'w+')
    except:
        pass
if os.path.exists('songs.zip'):
    os.remove('./songs.zip')
else:
    pass
destination = 'downloads'
song_file = open(file, 'r')
read_lines = song_file.readlines()
count = 0
for line in read_lines:
    count += 1
    try:
        print('Downloading....')
        song_formatted = ("{}".format(line.strip()))
        for k in song_formatted.split("\n"):
            song_line = re.sub(r"[^a-zA-Z0-9]+", ' ', k)
            song = song_line.replace(' ', '+')
            search_keyword=(song + '+lyrics')
            html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
            video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
            yt_link = ("https://www.youtube.com/watch?v=" + video_ids[0])
            yt = YouTube(str(yt_link))
            video = yt.streams.filter(only_audio=True).first()
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            try:
                remove_line()
            except:
                print(f"Couldn't remove {song_line}")		
    except Exception:
        error_file = open('error.txt', 'a')
        error = '{}: {} '.format(count, song_line)
        error_file.write(f'{error} \n')
print('Zipping...')
shutil.make_archive('songs', 'zip', './downloads/')
print('Clearing Downloads...')
shutil.rmtree('./downloads/')
print('Removing File...')
os.remove(file)