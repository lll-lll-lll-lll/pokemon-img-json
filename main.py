from xml.etree.ElementTree import indent
import cv2 as cv
import json
import numpy as np
import click

BLACK = 0
WHITE = 255

husigidane = "husigidane.png"
inputpath =  husigidane
outputpath = "jsons/" + "husigidane" + ".json"


def cvtCannyImg(img):
	edges = cv.Canny(img,100,200)
	return edges

def cvtPixelValToStr(img):
	H, W = img.shape
	strImg = []
	point = "*"
	blank = " "
	for y in range(H): 
		row = []
		for x in range(W):
			if img[x][y] == BLACK:
				row.insert(0,blank)
			elif img[x][y] == WHITE:
				row.insert(0,point)
		rowStr = "".join(row)
		strImg.append(rowStr)		
	return strImg

def saveToFile(imgStr, filepath):
	with open(filepath, "w") as f:
		json.dump(imgStr,f, indent=0)

def show(img):
	cv.imshow('window', img)
	cv.waitKey(30000)
	cv.destroyAllWindows()

# read img and rotate 90 degrees
def read_img(filename):
	dirs = "images/"
	img = cv.imread(dirs +filename)
	img = np.rot90(img)
	return img

# remove margin 
def preprocessedImg(grayImg):
	coords = cv.findNonZero(grayImg)
	x, y, w, h = cv.boundingRect(coords) 
	rect = img[y:y+h, x:x+w]
	return rect

if __name__ == "__main__":
	img = read_img(inputpath)
	print("hello")
	grayImg = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
	edgesImg = cvtCannyImg(grayImg)
	filterdStrImg = cvtPixelValToStr(edgesImg)
	saveToFile(filterdStrImg)