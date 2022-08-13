import cv2 as cv
import json
import numpy as np

Mat = np.ndarray[int, np.dtype[np.generic]]
BLACK = 0
WHITE = 255

husigidane = "husigidane.png"
pickchu = "pika.png"
gabigon = "gabigon.jpeg"
hitokage = "hitokage.png"
pika = "pika.png"
path = "images/" + gabigon

def cvtCannyImg(img: Mat):
	edges = cv.Canny(img,100,200)
	return edges


def joinOneRowStr(filterdStrImg):
	newStrImg = []
	for row in filterdStrImg:
		rowStr = "".join(row)
		newStrImg.append(rowStr)
	return newStrImg


def cvtPixelValToStr(img):
	strImg = []
	point = "*"
	blank = " "
	for y in range(len(img)): 
		row = []
		for x in range(len(img)):
			if img[x][y] == BLACK:
				row.append(blank)
			elif img[x][y] == WHITE:
				row.append(point)
		strImg.append(row)			
	return strImg
	

def show(img):
	cv.imshow('window', img)
	cv.waitKey(3000)
	cv.destroyAllWindows()

if __name__ == "__main__":
	img = cv.imread(path,0)
	grayImg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
	edgesImg = cvtCannyImg(grayImg)
	filterdStrImg = cvtPixelValToStr(edgesImg)
	joinedRowStr = joinOneRowStr(filterdStrImg)
	print(json.dumps(joinedRowStr, indent=4))
	
