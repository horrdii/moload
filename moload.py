import os
import subprocess
import platform
from time import sleep

from moviepy.editor import *
from pathlib import Path
from pytube import YouTube
from colorama import Fore, Back, Style, init
from sys import argv
from os import system, name


init()

try:
	if(subprocess.check_output(['uname', '-o']).strip() == b'Android'):
		SAVE_PATH = "/storage/emulated/0/Download/moload"
except:
	SAVE_PATH = str(Path.home() / "Downloads/moload")

if(platform.system() == "Windows"): clear = "cls"
else: clear = "clear"

streams = {}


def checkLink():
	try:
		link = argv[1]
	except:
		print(Fore.RED + 'Input in format "python moload.py {link}"')
		return False

	try:
		yt = YouTube(link)
	except:
		print("It's not a link")
		print(Fore.RED + 'Input in form "python moload.py {link}"')
		return False

	return True


def printMenu():
	_ = system(clear)
	print(Fore.GREEN + "Русский военный корабль, иди нахуй!\n")
	print(Fore.YELLOW + "In what format do you want to save this video?\n\n",
		Fore.GREEN + "[1]" + Fore.CYAN + " Video\n",
		Fore.GREEN + "[2]" + Fore.CYAN + " Audio\n",
		Fore.RED + "[3]" + Fore.MAGENTA + " Exit from the program\n\n")

	choise = input() 

	checkAnswer(choise)


def getTag(streams):
	_ = system(clear)
	i = 0
	print(Fore.YELLOW + "Choose format:\n")
	for i in range(len(streams) - 1):
		print(Fore.GREEN + f"[{i+1}]" + Fore.CYAN + f" {streams[i]}\n")
		i += 1
	print(Fore.RED + f'[{i+1}]' + Fore.MAGENTA + " Exit\n")

	tag = int(input())

	if(tag == i+1):
		printMenu()
		return "E"

	try:
		return streams[tag - 1].itag
	except:
		getRes()


def convertToMp3(type):
	winTitle = f"{title.replace(' ', '*')}"
	linTitle = f"'{title}.{type}'"

	video = VideoFileClip(os.path.join(SAVE_PATH, SAVE_PATH, f"{title}.{type}"))
	video.audio.write_audiofile(os.path.join(SAVE_PATH, SAVE_PATH, f"{title}.mp3"))
	print(SAVE_PATH.replace('\\', '/') + '/' + title)
	sleep(1)
	os.remove( os.path.join( SAVE_PATH, title + '.' + type ) )
	os.remove(SAVE_PATH.replace('\\', '/') + linTitle)


def vidDownload(type):
	if(type == "vid"):
		tag = getTag(streams.filter(type="video"))
	elif(type == "aud"):
		tag = getTag(streams.filter(type="video"))
		
	stream = streams.get_by_itag(tag)


	_ = system(clear)
	print(Fore.YELLOW + "Downloading " + title + '\n')	
	print(f'Video "{title}" downloaded to "{SAVE_PATH}"\n')

	stream.download(SAVE_PATH)
	if(type=="aud"): convertToMp3(stream.mime_type.split('/')[1])
	print(Fore.RED + "Some error")



def checkAnswer(choise):
	if(choise == "1"):
		vidDownload("vid")
	elif(choise == "2"):
		vidDownload("aud")
	elif(choise == "3"):
		print("Exit")
	else:
		printMenu()


if(checkLink()):
	streams = YouTube(argv[1]).streams
	title = streams[0].title

	resolutions = []


	for i in range(len(streams)):
		if(streams[i].resolution != None):
			resolutions.append(streams[i].resolution)

	resolutions = list(set(resolutions))
	resolutions.sort(reverse=False, key=lambda x: int(x[:len(x) - 2]))

	printMenu()