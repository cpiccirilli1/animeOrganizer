#!/usr/bin/python3/
import os, shutil, re
from pathlib import Path

home = str(Path.home())
src = os.path.join(home + '/Downloads/')
dest = os.path.join(home + '/Videos/Anime/')
moveCount = 0

fileReg = re.compile(r'(\[.*?\]\s)(.*?)(\[.*?\])')
folderReg = re.compile(r'[A-Za-z ]*[^- \d\d]')

print ('What extension would you like me to find?')
extension = input(": ")

def folderCreate(folder):
	mkFolder = os.path.join(dest, folder)
	if not os.path.isdir(mkFolder):
		os.mkdir(mkFolder)
		print('Made a folder for %s' % folder)
	else:
		print ('%s folder already exists' % folder)	

for i in os.listdir(src):
	if i.endswith(extension):
		start, end = os.path.splitext(os.path.join(i))
		fileName = fileReg.findall(i)
		folder = folderReg.findall(fileName[0][1])
		fileFix = fileName[0][1] + end
		fixFolderName = folder[0] 

		folderCreate(fixFolderName)
		shutil.move(os.path.join(src, i), os.path.join(dest, fixFolderName, fileFix))
		moveCount += 1

print ('Moved %d files.' % moveCount)