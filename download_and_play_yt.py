import file_path_adder
from random import randint
from os.path import realpath
from keyboard import read_key
from pywhatkit import playonyt
import pafy
import vlc

pth = realpath("favourites.txt")

url = playonyt(topic=input("Enter the topic:"),open_video=False)

video_data = pafy.new(url)
audio = video_data.getbestaudio()
audio.download()
stream_url = audio.url
print(stream_url)

Instance = vlc.Instance()
media = Instance.media_new(stream_url)
media.get_mrl()
player = Instance.media_player_new()
player.set_media(media)
player.play()
read_key()