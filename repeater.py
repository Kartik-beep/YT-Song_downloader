from pytube import YouTube
import os
import urllib.request
import re
import sys
import shutil

def remove_line():
    with open('songs.txt', 'r') as fr:
        lines = fr.readlines()
        ptr = 0
        with open('songs.txt', 'w') as fw:
            for line in lines:
                if ptr != 0:
                    fw.write(line)
                ptr += 1

if os.path.exists('songs.txt'):
    pass
else:
    try:
        open('songs.txt', 'w+')
        open('error.txt', 'w+')
        os.mkdir('Songs')
    except:
        pass
destination = 'Songs'
if os.path.exists('Songs'):
    shutil.rmtree('./Songs/')
else:
    pass
song = sys.argv
song_r = ' '.join(song)
song_name = song_r.replace('f:/My Python Projects/Yt To Mp3/repeater.py ', '')
print(song_name)
for k in song_name.split("\n"):
    song_line = re.sub(r"[^a-zA-Z0-9]+", ' ', k)
    if ' ' in song_line:
        song_artist = song_line.replace(' ', '+')
    else:
        pass
    search_keyword = (song_artist + '+audio')
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    yt_link = ("https://www.youtube.com/watch?v=" + video_ids[0])
    yt = YouTube(str(yt_link))
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)