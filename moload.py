import subprocess
import os

from moviepy.editor import *
from pathlib import Path
from pytube import YouTube
from colorama import Fore, Back, Style, init
from sys import argv
from os import system, name


init()

SAVE_PATH = str(Path.home() / "Downloads")
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
		print(Fore.RED + 'Input in format "python moload.py {link}"')
		return False

	return True


def printMenu():
	_ = system("cls")
	print(Fore.GREEN + "Русский военный корабль, иди нахуй!\n")
	print(Fore.YELLOW + "In what format do you want to save this video? ?\n",
		Fore.BLUE + "[1] MP4\n",
		Fore.BLUE + "[2] MP3\n",
		Fore.RED + "[3] Exit from the program\n")

	choise = input() 

	checkAnswer(choise)


def getRes():
	_ = system("cls")
	i = 0
	print(Fore.YELLOW + "In what resulution do you want this video?\n")
	for i in range(len(resolutions) - 1):
		print(Fore.BLUE + f"[{i+1}] {resolutions[i]}\n")
		i += 1
	print(Fore.RED + f'[{i+1}]' + " Exit")

	res = int(input())

	if(res == i+1):
		printMenu()
		return "E"

	try:
		return resolutions[res - 1]
	except:
		getRes()


def convertToMp3():
	video = VideoFileClip(os.path.join(SAVE_PATH, SAVE_PATH, f"{title}.mp4"), 0)
	video.audio.write_audiofile(os.path.join(SAVE_PATH, SAVE_PATH, f"{title}.mp3"))

def vidDownload(type):
	if(type == "mp4"):
		res = getRes()
		if(res == "E"):
			printMenu()
			return
		stream = streams.filter(file_extension='mp4', resolution=res)[0]

	elif(type == "mp3"):
		stream = streams.get_by_itag(18)
		stream.res = "144p"
		stream.abr = "128kbps"


	_ = system("cls")
	print(Fore.YELLOW + "Downloading " + title + '\n')	
	print(f'Video "{title}" downloaded to "{SAVE_PATH}"\n')
	stream.download(SAVE_PATH)
	if(type=="mp3"):
		convertToMp3()



def checkAnswer(choise):
	if(choise == "1"):
		vidDownload("mp4")
	elif(choise == "2"):
		vidDownload("mp3")
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