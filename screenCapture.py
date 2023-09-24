#sreenCapture.py

import time
import pyautogui
import threading
import os
from pathlib import Path

REPLAY_PATH = 'C:\\Users\\d73re\\Documents\\League of Legends\\Replays'
ROFLS = ['KR-6474121877.rofl', 'KR-6474155597.rofl', 'KR-6475627784.rofl', 'KR-6475874407.rofl', 'KR-6475988728.rofl'
		, 'KR-6476070057.rofl', 'KR-6476091827.rofl', 'KR-6476136025.rofl', 'KR-6476136702.rofl', 'KR-6476188059.rofl']
REPLAY_FILENAME = 'KR-6478964040.rofl'


GAMEWINDOW ='League of Legends (TM) Client'
WINDOW = (320, 180, 1280, 720)#left, top, width, height
GRAPHICS_FORMAT='.png'
SS_DELAY=1/1000.0
SS_NUMBER=60*60*40#frame * time

def screenshot(baseDir):
	#save screenshot
	for i in range(100000,100000+SS_NUMBER):
		t=time.perf_counter_ns()
		img=pyautogui.screenshot(region=WINDOW)
		img.save(baseDir+'/'+str(i)+str(t)+GRAPHICS_FORMAT)
		time.sleep(SS_DELAY)

def calculateTime(dir):
	gameLen = (int(os.listdir(dir)[-1][6:-4]) - int(os.listdir(dir)[0][6:-4])) / 1000000000
	(Path(dir)/Path(dir + '.txt')).write_text('Game Length:'+ str(gameLen))

def main():
	originalPath = Path(REPLAY_PATH)/Path(REPLAY_FILENAME)
	tempPath = Path(REPLAY_PATH)/Path(REPLAY_FILENAME + '0')
	os.rename(originalPath, tempPath)#rename replay
	
	for rofl in ROFLS:
		replaydir = rofl[:-5]
		os.mkdir(replaydir)
		os.rename(Path(REPLAY_PATH)/Path(rofl), originalPath)

		input('click replay button and press any key to start[press '4']')#user input to start caputre
		try:
			time.sleep(3)#loading time
			screenshot(replaydir)
		except KeyboardInterrupt:
			print('record finished')#CTRL+C to finish capture
		calculateTime(replaydir)

		os.rename(originalPath, Path(REPLAY_PATH)/Path(rofl))

	os.rename(tempPath, originalPath)#return to oldname

if __name__ == '__main__':
	main()
