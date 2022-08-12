import cv2 as cv
import numpy as np

Mat = np.ndarray[int, np.dtype[np.generic]]

husigidane = "husigidane.png"
pickchu = "pika.png"
gabigon = "gabigon.jpeg"
hitokage = "hitokage.png"
path = "images/" + husigidane

def cvtCannyImg(img: Mat):
	edges = cv.Canny(img,100,200)
	return edges

if __name__ == "__main__":
	img = cv.imread(path,0)
	grayImg = cv.cvtColor(img, cv.COLOR_BGR2RGB)
	edgesImg = cvtCannyImg(grayImg)
	cv.imshow('window', edgesImg)
	cv.waitKey(3000)
	cv.destroyAllWindows()