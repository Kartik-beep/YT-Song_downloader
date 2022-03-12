from pytube import YouTube
import os
import urllib.request
import re

def remove_line():
    with open('songs.txt', 'r') as fr:
        lines = fr.readlines()
        ptr = 0
        with open('songs.txt', 'w') as fw:
            for line in lines:
                if ptr != 0:
                    fw.write(line)
                ptr += 1

def converter():
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
	use_file = str(input('do you want to use the file(type Yes or No):')).lower()
	if 'yes' in use_file:
		song_file = open('songs.txt', 'r')
		read_lines = song_file.readlines()
		count = 0
		for line in read_lines:
			count += 1
			try:
				print(count)
				song_formatted = ("{}".format(line.strip()))
				for k in song_formatted.split("\n"):
					song_line = re.sub(r"[^a-zA-Z0-9]+", ' ', k)
					if ' ' in song_line:
						song = song_line.replace(' ', '+')
					else:
						pass
					search_keyword=(song + '+audio')
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
				print(f'{error}')
	else:
		name_or_link = str(input('Do you have link?(Type Yes or No):')).lower()
		if 'yes' in name_or_link:
			link = str(input("Please paste the link:"))
			yt = YouTube(link)
			video = yt.streams.filter(only_audio=True).first()
			out_file = video.download(output_path=destination)
			base, ext = os.path.splitext(out_file)
			new_file = base + '.mp3'
			os.rename(out_file, new_file)
		else:
			song_name = str(input("Please Type the name of song and artist:"))
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
converter()