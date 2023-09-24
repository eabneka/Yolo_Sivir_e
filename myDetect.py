#myDetect.py
import torch
import os
from pathlib import Path

IMAGE_DIRECTORY = '../replay_capture'

model = torch.hub.load('ultralytics/yolov5', 'custom', path='../yolov5/runs/train/exp4/weights/last.pt', force_reload=True)

def elapsed(later, former):
	return (int(later[6:-4]) - int(former[6:-4])) / 1000000000


for dir in os.listdir(IMAGE_DIRECTORY):
	if(dir == 'screenCapture.py'):
		continue

	imgDir=Path(IMAGE_DIRECTORY)/Path(dir)#replay file

	imgList=sorted(imgDir.glob('*.png'))#list of png
	text = open(imgDir/Path(dir+'.txt'), 'a')
	begin = imgList[0]
	e_detected = 0
	emptylist =[]

	for img in imgList:
		li = model(Path(img)).xyxyn[0].detach().tolist()
		if(li == []):
			continue


		if(li[0][5] == 1):#e successful
			if(e_detected == 0):
				time = elapsed(img,begin)
				text.write('time(s): ' + str(time) +'success\n')
			elif(elapsed(img,e_detected) < 3):
				time = elapsed(e_detected,begin)
				text.write('time(s): ' + str(time) +'fail\n')
				e_detected = 0
		elif(li[0][5] == 0):#e activated
			if(e_detected == 0):
				e_detected = img
			elif(elapsed(img,e_detected) >= 3):
				time(e_detected,begin)
				text.write('time(s): ' + str(time) +'fail\n')
				e_detected = 0

	text.close()
